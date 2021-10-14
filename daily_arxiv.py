import datetime
import time
import requests
import json
from datetime import timedelta
import arxiv
import os

base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"

def get_authors(authors, first_author = False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output

def get_daily_code(DateToday,query="slam", max_results=2):
    """
    @param DateToday: str
    @param query: str
    @return paper_with_code: dict
    """

    # output 
    content = dict() 
    content_to_web = dict()

    # content
    output = dict()
    
    search_engine = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    cnt = 0

    for result in search_engine.results():

        paper_id       = result.get_short_id()
        paper_title    = result.title
        paper_url      = result.entry_id

        code_url       = base_url + paper_id
        paper_abstract = result.summary.replace("\n"," ")
        paper_authors  = get_authors(result.authors)
        paper_first_author = get_authors(result.authors,first_author = True)
        primary_category = result.primary_category

        publish_time = result.published.date()

      
        print("Time = ", publish_time ,
              " title = ", paper_title,
              " author = ", paper_first_author)

        # eg: 2108.09112v1 -> 2108.09112
        ver_pos = paper_id.find('v')
        if ver_pos == -1:
            paper_key = paper_id
        else:
            paper_key = paper_id[0:ver_pos]    

        try:
            r = requests.get(code_url).json()
            # source code link
            if "official" in r and r["official"]:
                cnt += 1
                repo_url = r["official"]["url"]
                # content[paper_key] = f"|**{publish_time}**|**{paper_title}**|{paper_abstract}|{paper_authors}|[{paper_id}]({paper_url})|**[link]({repo_url})**|\n"
                content[paper_key] = f"|**{publish_time}**|**{paper_title}**|{paper_first_author} et.al.|[{paper_id}]({paper_url})|**[link]({repo_url})**|\n"
                content_to_web[paper_key] = f"- **{publish_time}**, **{paper_title}**, {paper_first_author} et.al., [PDF:{paper_id}]({paper_url}), **[code]({repo_url})**\n"
            else:
                # content[paper_key] = f"|**{publish_time}**|**{paper_title}**|{paper_abstract}|{paper_authors}|[{paper_id}]({paper_url})|null|\n"
                content[paper_key] = f"|**{publish_time}**|**{paper_title}**|{paper_first_author} et.al.|[{paper_id}]({paper_url})|null|\n"
                content_to_web[paper_key] = f"- **{publish_time}**, **{paper_title}**, {paper_first_author} et.al., [PDF:{paper_id}]({paper_url})\n"

        except Exception as e:
            print(f"exception: {e} with id: {paper_key}")

    data = {DateToday:content}
    data_web = {DateToday:content_to_web}
    return data,data_web 

def update_daily_json(filename,data_all):
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
            
    for data in data_all:
        m.update(data)

    with open(filename,"w") as f:
        json.dump(m,f)
    
def json_to_md(filename,to_web = False):
    """
    @param filename: str
    @return None
    """

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    if to_web == False:
        md_filename = "README.md"  
    else:
        md_filename = "./docs/index.md"  
                  
    # clean README.md if daily already exist else create it
    with open(md_filename,"w+") as f:
        pass

    # write data into README.md
    with open(md_filename,"a+") as f:

        if to_web == True:
            f.write("---\n" + "layout: default\n" + "---\n\n")

        for day in data.keys():
            day_content = data[day]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {day}\n\n")

            if to_web == False:
                f.write("|Publish Date|Title|Authors|PDF|Code|\n" + "|---|---|---|---|---|\n")
            else:
                f.write("| Publish Date | Title | Authors | PDF | Code |\n")
                f.write("|:---------|:-----------------------|:---------|:------|:------|\n")

            for _,v in day_content.items():
                if v is not None:
                    f.write(v)

            f.write(f"\n")

    print("finished")        

 

if __name__ == "__main__":

    DateNow = datetime.date.today()

    data_collector = []
    data_collector_web= []
    
    keywords = dict()
    keywords["SLAM"]                = "SLAM"
    keywords["SFM"]                 = "SFM"+"OR"+"\"Structure from Motion\""
    keywords["Visual Localization"] = "\"Camera Localization\"OR\"Visual Localization\"OR\"Camera Re-localisation\""
    keywords["Keypoint Detection"]  = "\"Keypoint Detection\"OR\"Feature Descriptor\""
    keywords["Image Matching"]      = "\"Image Matching\""

    for topic,keyword in keywords.items():
 
        # topic = keyword.replace("\"","")
        print("Keyword: " + topic)

        data,data_web = get_daily_code(topic, query = keyword, max_results = 10)
        data_collector.append(data)
        data_collector_web.append(data_web)

        print("\n")

    # update README.md file
    json_file = "cv-arxiv-daily.json"
#     if ~os.path.exists(json_file):
#         with open(json_file,'w')as a:
#             print("create " + json_file)

    # update json data
    update_daily_json(json_file,data_collector)
    # json data to markdown
    json_to_md(json_file)

    # update docs/index.md file
    json_file = "./docs/cv-arxiv-daily-web.json"
#     if ~os.path.exists(json_file):
#         with open(json_file,'w')as a:
#             print("create " + json_file)

    # update json data
    update_daily_json(json_file,data_collector)
    # json data to markdown
    json_to_md(json_file, to_web = True)
