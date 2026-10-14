import os
import re
import json
import arxiv
import yaml
import logging
import argparse
import datetime
import requests
import time

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

github_code_search_url = "https://api.github.com/search/code"
hf_papers_url = "https://huggingface.co/api/papers/"
arxiv_url = "http://arxiv.org/"

def load_config(config_file:str) -> dict:
    '''
    config_file: input config file path
    return: a dict of configuration
    '''
    # make filters pretty
    def pretty_filters(**config) -> dict:
        keywords = dict()
        EXCAPE = '\"'
        QUOTA = '' # NO-USE
        OR = ' OR ' # TODO
        def parse_filters(filters:list):
            ret = ''
            for idx in range(0,len(filters)):
                filter = filters[idx]
                if len(filter.split()) > 1:
                    ret += (EXCAPE + filter + EXCAPE)
                else:
                    ret += (QUOTA + filter + QUOTA)
                if idx != len(filters) - 1:
                    ret += OR
            return ret
        # optional arxiv categories (eg. cs.CV), per keyword or for all keywords
        default_categories = config.get('categories', [])
        categories = dict()
        for k,v in config['keywords'].items():
            query = parse_filters(v['filters'])
            categories[k] = v.get('categories', default_categories)
            if categories[k]:
                cats = OR.join('cat:' + c for c in categories[k])
                query = f'({query}) AND ({cats})'
            keywords[k] = query
        return keywords, categories
    with open(config_file,'r') as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
        config['kv'], config['kc'] = pretty_filters(**config)
        logging.info(f'config = {config}')
    return config

def get_authors(authors, first_author = False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output
def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output
# ---------------------------------------------------------------------------
# code links. PapersWithCode is gone, github repos are looked up from (in order):
#   1. the paper's abstract / comment (free, arxiv already returns them)
#   2. Hugging Face papers API (it took over the PapersWithCode data)
#   3. GitHub code search for the arxiv id in README files (needs GITHUB_TOKEN,
#      10 requests per minute, only used by the weekly update)
# ---------------------------------------------------------------------------
GITHUB_REPO_RE = re.compile(r'(?:https?://)?(?:www\.)?github\.com/([\w.-]+/[\w.-]+)', re.I)
# repos that merely cite papers in their README: paper lists, arxiv daily bots, model zoos...
NOT_CODE_REPO_RE = re.compile(r'awesome|paper|arxiv|daily|weekly|survey|list|zoo|reading|collection|notes?$|favor|track', re.I)
code_link_cache = dict()    # arxiv_id -> (code url or None, thorough), the json files share the lookups
github_search_state = {
    'last': 0.0,            # time of the last request
    'remaining': None,      # X-RateLimit-Remaining of the last response
    'reset': 0.0,           # X-RateLimit-Reset of the last response
    'deadline': None,       # no more searches after this time, see set_github_search_budget
    'logged_limit': False,
}

def set_github_search_budget(minutes:float):
    '''
    stop searching GitHub after these minutes (the weekly job must finish in reasonable time)
    '''
    github_search_state['deadline'] = time.time() + 60 * minutes

def format_code_link(code_url) -> str:
    return f"**[link]({code_url})**" if code_url else 'null'

def get_code_link_from_text(text:str) -> str:
    '''
    first github repo mentioned in the abstract / comment of a paper, None if none
    '''
    for match in GITHUB_REPO_RE.finditer(text or ''):
        repo = re.sub(r'(\.git)?\.?$', '', match.group(1))
        return 'https://github.com/' + repo
    return None

def get_code_link_from_hf(arxiv_id:str) -> str:
    '''
    github repo of a paper on Hugging Face papers (huggingface.co/papers/<arxiv_id>), None if none
    '''
    try:
        r = requests.get(hf_papers_url + arxiv_id, timeout = 20)
        if r.status_code != 200:
            return None
        return r.json().get('githubRepo') or None
    except (requests.RequestException, ValueError) as e:
        logging.warning(f'Hugging Face lookup failed for {arxiv_id}: {e}')
        return None

def get_code_link_from_github(arxiv_id:str, title:str = '') -> str:
    '''
    search github README files citing the arxiv id (needs GITHUB_TOKEN), None if none.
    Many repos cite papers they do not implement, so a repo is only accepted when its
    name matches the title prefix (eg. "MatchAnything: Universal..." -> MatchAnything)
    or it is the only remaining repo citing the paper in its root README
    '''
    state = github_search_state
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        return None
    if state['deadline'] and time.time() > state['deadline']:
        return None
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json'}
    params = {'q': f'"{arxiv_id}" filename:README.md', 'per_page': 30}
    for _ in range(2):
        # code search allows 10 requests per minute (less for some tokens): wait for the
        # window to reset when the last response said the quota is used up
        wait = 0
        if state['remaining'] == 0:
            wait = state['reset'] - time.time()
        wait = max(wait, state['last'] + 6.5 - time.time(), 0)
        time.sleep(min(wait, 120))
        state['last'] = time.time()
        try:
            r = requests.get(github_code_search_url, params = params, headers = headers, timeout = 30)
        except requests.RequestException as e:
            logging.warning(f'GitHub code search failed for {arxiv_id}: {e}')
            return None
        if 'X-RateLimit-Remaining' in r.headers:
            state['remaining'] = int(r.headers['X-RateLimit-Remaining'])
            state['reset'] = float(r.headers.get('X-RateLimit-Reset', 0))
        if r.status_code in (403, 429):
            if not state['logged_limit']:
                state['logged_limit'] = True
                limits = {k: v for k, v in r.headers.items() if k.lower().startswith(('x-ratelimit', 'retry-after'))}
                logging.warning(f'GitHub code search rate limited: {limits} {r.text[:200]}')
            retry_after = float(r.headers.get('Retry-After', 0))
            wait = max(retry_after, state['reset'] - time.time(), 1)
            logging.warning(f'GitHub code search rate limited, sleeping {wait:.0f}s')
            time.sleep(min(wait, 120))
            state['remaining'] = None
            continue
        if r.status_code != 200:
            logging.warning(f'GitHub code search failed for {arxiv_id} ({r.status_code}): {r.text[:200]}')
            return None
        break
    else:
        return None

    normalize = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
    name = normalize(title.split(':')[0]) if ':' in title else ''
    root_readme_repos = []
    for item in r.json().get('items', []):
        repo = item['repository']
        # skip forks, paper lists and profile READMEs (repo named after its owner)
        if repo.get('fork') or NOT_CODE_REPO_RE.search(repo['name']) \
                or repo['name'].lower() == repo['owner']['login'].lower():
            continue
        repo_name = normalize(repo['name'])
        if len(name) >= 3 and len(repo_name) >= 3 and (name in repo_name or repo_name in name):
            return repo['html_url']
        if item['path'].lower() == 'readme.md':
            root_readme_repos.append(repo['html_url'])
    if len(root_readme_repos) == 1:
        return root_readme_repos[0]
    return None

def get_code_link(arxiv_id:str, title:str = '', text:str = '', thorough = False) -> str:
    '''
    @param text: abstract / comment of the paper to grep github links from
    @param thorough: also search GitHub (slow, 10 requests per minute), for the weekly update
    @return code url, None if not found
    '''
    if arxiv_id in code_link_cache:
        code_url, was_thorough = code_link_cache[arxiv_id]
        if code_url or was_thorough or not thorough:
            return code_url
    code_url = get_code_link_from_text(text)
    if code_url is None:
        code_url = get_code_link_from_hf(arxiv_id)
    if code_url is None and thorough:
        code_url = get_code_link_from_github(arxiv_id, title)
    code_link_cache[arxiv_id] = (code_url, thorough)
    return code_url

def get_paper_texts(arxiv_ids:list) -> dict:
    '''
    abstract + comment of papers by arxiv id (arxiv takes up to 100 ids per request)
    '''
    texts = dict()
    client = arxiv.Client(page_size = 100, delay_seconds = 3, num_retries = 5)
    for i in range(0, len(arxiv_ids), 100):
        batch = arxiv_ids[i:i+100]
        try:
            for result in client.results(arxiv.Search(id_list = batch, max_results = len(batch))):
                paper_key = re.sub(r'v\d+$', '', result.get_short_id())
                texts[paper_key] = (result.summary or '') + ' ' + (result.comment or '')
        except Exception:
            logging.exception(f'Failed to fetch abstracts of {batch[0]}..{batch[-1]}')
    return texts

def get_daily_papers(topic,query="slam", max_results=2, categories=None):
    """
    @param topic: str
    @param query: str
    @param categories: only keep papers whose primary category is in this list, None for all
                       (the query's cat: filter also matches cross-listed categories)
    @return paper_with_code: dict
    """
    # output
    content = dict()
    content_to_web = dict()
    search_engine = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    # arxiv>=2.0 removed Search.results(), queries go through a Client now
    client = arxiv.Client(page_size = max_results, delay_seconds = 3, num_retries = 5)

    for result in client.results(search_engine):

        paper_id            = result.get_short_id()
        paper_title         = result.title
        paper_url           = result.entry_id
        paper_abstract      = result.summary.replace("\n"," ")
        paper_authors       = get_authors(result.authors)
        paper_first_author  = get_authors(result.authors,first_author = True)
        primary_category    = result.primary_category
        publish_time        = result.published.date()
        update_time         = result.updated.date()
        comments            = result.comment

        if categories and primary_category not in categories:
            logging.info(f"Skip {paper_id} ({primary_category} not in {categories}): {paper_title}")
            continue

        logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

        # eg: 2108.09112v1 -> 2108.09112
        ver_pos = paper_id.find('v')
        if ver_pos == -1:
            paper_key = paper_id
        else:
            paper_key = paper_id[0:ver_pos]
        paper_url = arxiv_url + 'abs/' + paper_key

        # cheap lookups only (abstract + Hugging Face), the weekly update searches GitHub
        code_url = get_code_link(paper_key, paper_title, paper_abstract + ' ' + (comments or ''))
        if code_url:
            logging.info(f"Code of {paper_key}: {code_url}")

        content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|{}|\n".format(
               update_time,paper_title,paper_first_author,paper_key,paper_url,format_code_link(code_url))
        content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
               update_time,paper_title,paper_first_author,paper_url,paper_url)
        if code_url:
            content_to_web[paper_key] += ", Code: **[{}]({})**".format(code_url,code_url)

        # TODO: select useful comments
        comments = None
        if comments != None:
            content_to_web[paper_key] += f", {comments}\n"
        else:
            content_to_web[paper_key] += f"\n"

    data = {topic:content}
    data_web = {topic:content_to_web}
    return data,data_web

def update_paper_links(filename, code_check_days = 180, max_code_checks = 300, code_checks_path = None):
    '''
    weekly update paper links in json file: look up the code of papers without one
    @param code_check_days: only papers published within these days, <= 0 for all
    @param max_code_checks: max papers to look up per run (GitHub allows 10 searches per
                            minute), the least recently checked papers first
    @param code_checks_path: json file remembering when each paper was last checked
    '''
    def parse_arxiv_string(s):
        parts = s.split("|")
        date = parts[1].strip()
        title = parts[2].strip()
        authors = parts[3].strip()
        arxiv_id = parts[4].strip()
        code = parts[5].strip()
        arxiv_id = re.sub(r'v\d+', '', arxiv_id)
        return date,title,authors,arxiv_id,code

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

    json_data = m.copy()

    code_checks = dict()
    if code_checks_path and os.path.exists(code_checks_path):
        with open(code_checks_path, "r") as f:
            code_checks = json.load(f)

    today = datetime.date.today()
    candidates = []
    for keywords,v in json_data.items():
        for paper_id,contents in v.items():
            contents = str(contents)
            if not contents.startswith('|'):
                continue
            update_time, paper_title, paper_first_author, paper_url, code_url = parse_arxiv_string(contents)
            if code_url != 'null':
                continue
            try:
                date = datetime.date.fromisoformat(update_time.strip('*'))
            except ValueError:
                date = today
            if code_check_days > 0 and (today - date).days > code_check_days:
                continue
            candidates.append((keywords, paper_id, paper_title.strip('*'), date))

    # least recently checked first, newest papers first; papers already checked today
    # are looked up again first since their results are cached (the json files share them)
    def priority(candidate):
        last_check = code_checks.get(candidate[1], '')
        return (last_check != str(today), last_check, -candidate[3].toordinal())
    candidates.sort(key = priority)
    candidates = candidates[:max_code_checks]
    logging.info(f'{filename}: looking up the code of {len(candidates)} papers')

    texts = get_paper_texts(sorted(set(c[1] for c in candidates)))
    num_found = 0
    for keywords, paper_id, paper_title, _ in candidates:
        code_url = get_code_link(paper_id, paper_title, texts.get(paper_id, ''), thorough = True)
        code_checks[paper_id] = str(today)
        if code_url is None:
            continue
        num_found += 1
        parts = json_data[keywords][paper_id].split("|")
        parts[5] = format_code_link(code_url)
        json_data[keywords][paper_id] = "|".join(parts)
        logging.info(f'Code of {paper_id}: {code_url}')
    logging.info(f'{filename}: found the code of {num_found} papers')

    # dump to json file
    with open(filename,"w") as f:
        json.dump(json_data,f)
    if code_checks_path:
        with open(code_checks_path,"w") as f:
            json.dump(code_checks,f)

def update_json_file(filename,data_dict):
    '''
    daily update json file using data_dict
    '''
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

    json_data = m.copy()

    # update papers in each keywords
    for data in data_dict:
        for keyword in data.keys():
            papers = data[keyword]

            if keyword in json_data.keys():
                json_data[keyword].update(papers)
            else:
                json_data[keyword] = papers

    with open(filename,"w") as f:
        json.dump(json_data,f)

def pretty_math(s:str) -> str:
    ret = ''
    match = re.search(r"\$.*\$", s)
    if match == None:
        return s
    math_start,math_end = match.span()
    space_trail = space_leading = ''
    if s[:math_start][-1] != ' ' and '*' != s[:math_start][-1]: space_trail = ' '
    if s[math_end:][0] != ' ' and '*' != s[math_end:][0]: space_leading = ' '
    ret += s[:math_start]
    ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
    ret += s[math_end:]
    return ret

def md_anchor(heading:str) -> str:
    '''
    github anchor of a markdown heading, eg. "Updated on 2026.10.12" -> #updated-on-20261012
    '''
    return '#' + re.sub(r'[^\w\- ]', '', heading).replace(' ','-').lower()

def get_paper_year(paper:str) -> str:
    '''
    year of a paper entry, parsed from its publish date, eg. |**2026-05-13**|... -> 2026
    '''
    match = re.search(r'(\d{4})-\d{2}-\d{2}', paper)
    if match == None:
        return str(datetime.date.today().year)
    return match.group(1)

def split_by_year(data:dict) -> dict:
    '''
    {keyword: {paper_id: paper}} -> {year: {keyword: {paper_id: paper}}}, latest year first
    '''
    by_year = dict()
    for keyword, papers in data.items():
        for paper_id, paper in papers.items():
            if paper is None:
                continue
            year = get_paper_year(paper)
            by_year.setdefault(year, dict()).setdefault(keyword, dict())[paper_id] = paper
    return {year: by_year[year] for year in sorted(by_year.keys(), reverse=True)}

def write_md_table(f, papers:dict, to_web = False, use_title = True, max_papers = None):
    '''
    write the papers of one keyword as a markdown table, latest first
    @param max_papers: only write the latest max_papers papers, None for all
    '''
    if use_title == True :
        if to_web == False:
            f.write("|Publish Date|Title|Authors|PDF|Code|\n" + "|---|---|---|---|---|\n")
        else:
            f.write("| Publish Date | Title | Authors | PDF | Code |\n")
            f.write("|:---------|:-----------------------|:---------|:------|:------|\n")

    # sort papers by date
    papers = sort_papers(papers)

    for idx,(_,v) in enumerate(papers.items()):
        if max_papers != None and idx >= max_papers:
            break
        if v is not None:
            if to_web == True:
                # a muted dash instead of "null" in the code column
                v = v.replace('|null|\n', '|<span class="null">—</span>|\n')
            f.write(pretty_math(v)) # make latex pretty

def write_archive(data:dict, archive_dir:str) -> dict:
    '''
    archive all papers by year, one markdown per keyword plus an index per year:
        archive_dir/<year>/README.md
        archive_dir/<year>/<Keyword>.md
    github stops rendering markdown beyond 512 KB, so a whole year does not fit in one file.
    The files are plain markdown shared by github and the gitpage: jekyll renders them
    without front matter and turns the .md links into .html (both are github pages defaults)
    @return {year: {keyword: (num_papers, filename)}}, latest year first
    '''
    archive = dict()
    for year, year_data in split_by_year(data).items():
        year_dir = os.path.join(archive_dir, year)
        os.makedirs(year_dir, exist_ok=True)
        archive[year] = dict()

        for keyword, papers in year_data.items():
            name = keyword.replace(' ','-') + '.md'
            heading = f"{keyword} ({year})"
            with open(os.path.join(year_dir, name), "w") as f:
                f.write(f"## {heading}\n")
                f.write(f"> {len(papers)} papers, [archive {year}](./README.md)\n\n")
                write_md_table(f, papers, to_web = True)   # github renders the dash span too
                f.write(f"\n")
                f.write(f"<p align=right>(<a href={md_anchor(heading)}>back to top</a>)</p>\n\n")
            archive[year][keyword] = (len(papers), name)

        # the index of this year
        with open(os.path.join(year_dir, "README.md"), "w") as f:
            f.write(f"## Archive {year}\n")
            total = sum(n for n,_ in archive[year].values())
            f.write(f"> {total} papers\n\n")
            f.write("|Keyword|Papers|\n" + "|---|---|\n")
            for keyword,(n,link) in archive[year].items():
                f.write(f"|[{keyword}](./{link})|{n}|\n")
            f.write(f"\n")
        logging.info(f"archived {total} papers of {year} to {year_dir}")
    return archive

def write_archive_table(f, archive:dict, keywords:list, archive_link:str, to_web = False):
    '''
    write the year x keyword table linking to the archived markdown files
    '''
    f.write("## Archive {#archive}\n\n" if to_web else "## Archive\n\n")
    f.write("> All papers, one markdown per year and keyword.\n\n")
    f.write("|Year|" + "|".join(keywords) + "|\n")
    f.write("|---|" + "|".join("---" for _ in keywords) + "|\n")
    for year, year_archive in archive.items():
        f.write(f"|[{year}]({archive_link}/{year}/README.md)|")
        for keyword in keywords:
            if keyword in year_archive:
                n, link = year_archive[keyword]
                f.write(f"[{n}]({archive_link}/{year}/{link})")
            f.write("|")
        f.write("\n")
    f.write("\n")

def json_to_md(filename,md_filename,
               task = '',
               to_web = False,
               use_title = True,
               use_tc = True,
               show_badge = True,
               use_b2t = True,
               max_papers = None,
               archive_dir = None):
    """
    @param filename: str
    @param md_filename: str
    @param max_papers: only keep the latest max_papers papers of each keyword in md_filename,
                       None for all (github stops rendering markdown beyond 512 KB)
    @param archive_dir: archive all papers by year under this folder, None to skip
    @return None
    """
    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-','.')

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    archive = None
    if archive_dir != None:
        archive = write_archive(data, archive_dir)
        archive_link = './' + os.path.relpath(archive_dir, os.path.dirname(md_filename) or '.')

    # clean README.md if daily already exist else create it
    with open(md_filename,"w+") as f:
        pass

    # write data into README.md
    with open(md_filename,"a+") as f:

        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")

        # if show_badge == True:
        #     f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
        #     f.write(f"[![Forks][forks-shield]][forks-url]\n")
        #     f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
        #     f.write(f"[![Issues][issues-shield]][issues-url]\n\n")

        usage_link = './' + os.path.relpath('docs/README.md', os.path.dirname(md_filename) or '.')
        keywords = [keyword for keyword, papers in data.items() if papers]

        if to_web == True:
            # the gitpage layout (docs/_layouts/default.html) styles these: a meta line
            # and keyword chips instead of the heading and the table of contents
            # raw html links are not rewritten by jekyll-relative-links, link the html directly
            f.write(f'<p class="meta">Updated on {DateNow} · <a href="{usage_link[:-3]}.html#usage">Usage</a></p>\n\n')
            f.write('<nav class="toc">\n')
            for keyword in keywords:
                f.write(f'<a href="#{md_anchor(keyword)[1:]}">{keyword}</a>\n')
            if archive != None:
                f.write('<a href="#archive" class="archive">Archive</a>\n')
            f.write('</nav>\n\n')
        elif use_title == True:
            #f.write(("<p align="center"><h1 align="center"><br><ins>CV-ARXIV-DAILY"
            #         "</ins><br>Automatically Update CV Papers Daily</h1></p>\n"))
            f.write("## Updated on " + DateNow + "\n")
            f.write(f"> Usage instructions: [here]({usage_link}#usage)\n\n")
        else:
            f.write("> Updated on " + DateNow + "\n")
            f.write(f"> Usage instructions: [here]({usage_link}#usage)\n\n")

        #Add: table of contents
        if use_tc == True and to_web == False:
            f.write("<details>\n")
            f.write("  <summary>Table of Contents</summary>\n")
            f.write("  <ol>\n")
            if archive != None:
                f.write(f"    <li><a href=#archive>Archive</a></li>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ','-')
                f.write(f"    <li><a href=#{kw.lower()}>{keyword}</a></li>\n")
            f.write("  </ol>\n")
            f.write("</details>\n\n")

        if archive != None:
            write_archive_table(f, archive, keywords, archive_link, to_web = to_web)

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            # the head of each part (explicit id for kramdown, which drops leading digits)
            if to_web == True:
                f.write(f"## {keyword} {{#{md_anchor(keyword)[1:]}}}\n\n")
            else:
                f.write(f"## {keyword}\n\n")

            write_md_table(f, day_content, to_web = to_web, use_title = use_title,
                           max_papers = max_papers)

            f.write(f"\n")

            if max_papers != None and len(day_content) > max_papers:
                f.write((f"> Showing the latest {max_papers} of {len(day_content)} papers, "
                         f"see the [archive](#archive) for all.\n\n"))

            #Add: back to top
            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ','-').replace('.','')
                f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")

        if show_badge == True:
            # we don't like long string, break it!
            f.write((f"[contributors-shield]: https://img.shields.io/github/"
                     f"contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[contributors-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/graphs/contributors\n"))
            f.write((f"[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[forks-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/network/members\n"))
            f.write((f"[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[stars-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/stargazers\n"))
            f.write((f"[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[issues-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/issues\n\n"))

    logging.info(f"{task} finished")

def demo(**config):
    # TODO: use config
    data_collector = []
    data_collector_web= []

    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    publish_gitpage = config['publish_gitpage']
    publish_wechat = config['publish_wechat']
    show_badge = config['show_badge']
    max_papers = config.get('max_papers_in_readme', None)
    code_check_args = {
        'code_check_days': config.get('code_check_days', 180),
        'max_code_checks': config.get('max_code_checks', 300),
        'code_checks_path': config.get('code_checks_path', None),
    }

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    if b_update:
        set_github_search_budget(config.get('max_code_search_minutes', 40))
    if config['update_paper_links'] == False:
        logging.info(f"GET daily papers begin")
        num_papers = 0
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}")
            # one failing query (arxiv is flaky) should not block the other keywords
            try:
                data, data_web = get_daily_papers(topic, query = keyword,
                                                max_results = max_results,
                                                categories = config['kc'][topic])
            except Exception:
                logging.exception(f"Failed to get papers of keyword: {topic}")
                continue
            num_papers += len(data[topic])
            data_collector.append(data)
            data_collector_web.append(data_web)
            print("\n")
        logging.info(f"GET daily papers end")
        if num_papers == 0:
            raise RuntimeError("No papers fetched for any keyword, see the errors above")

    # 1. update README.md file
    if publish_readme:
        json_file = config['json_readme_path']
        md_file   = config['md_readme_path']
        # update paper links
        if config['update_paper_links']:
            update_paper_links(json_file, **code_check_args)
        else:
            # update json data
            update_json_file(json_file,data_collector)
        # json data to markdown
        json_to_md(json_file,md_file, task ='Update Readme', \
            show_badge = show_badge, max_papers = max_papers, \
            archive_dir = config.get('archive_dir', None))

    # 2. update docs/index.md file (to gitpage)
    if publish_gitpage:
        json_file = config['json_gitpage_path']
        md_file   = config['md_gitpage_path']
        # TODO: duplicated update paper links!!!
        if config['update_paper_links']:
            update_paper_links(json_file, **code_check_args)
        else:
            update_json_file(json_file,data_collector)
        json_to_md(json_file, md_file, task ='Update GitPage', \
            to_web = True, show_badge = show_badge, \
            use_tc=False, use_b2t=False, max_papers = max_papers, \
            archive_dir = config.get('archive_dir', None))

    # 3. Update docs/wechat.md file
    if publish_wechat:
        json_file = config['json_wechat_path']
        md_file   = config['md_wechat_path']
        # TODO: duplicated update paper links!!!
        if config['update_paper_links']:
            update_paper_links(json_file, **code_check_args)
        else:
            update_json_file(json_file, data_collector_web)
        json_to_md(json_file, md_file, task ='Update Wechat', \
            to_web=False, use_title= False, show_badge = show_badge)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path',type=str, default='config.yaml',
                            help='configuration file path')
    parser.add_argument('--update_paper_links', default=False,
                        action="store_true",help='whether to update paper links etc.')
    parser.add_argument('--code_check_days', type=int, default=None,
                        help='with --update_paper_links: only papers within these days, <= 0 for all (overrides config)')
    parser.add_argument('--max_code_checks', type=int, default=None,
                        help='with --update_paper_links: max papers to look up (overrides config)')
    args = parser.parse_args()
    config = load_config(args.config_path)
    config = {**config, 'update_paper_links':args.update_paper_links}
    if args.code_check_days is not None:
        config['code_check_days'] = args.code_check_days
    if args.max_code_checks is not None:
        config['max_code_checks'] = args.max_code_checks
    demo(**config)
