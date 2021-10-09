# refer to github@zhuwenxing/daily_arxiv

import arxivscraper
import datetime
import time
import requests
import json
from datetime import timedelta


def get_daily_code(DateToday,cats):
    """
    @param DateToday: str
    @param cats: dict
    @return paper_with_code: dict
    """
    from_day = until_day = DateToday
    content = dict()
    # content
    output = dict()
    for k,v in cats.items():
        scraper = arxivscraper.Scraper(category=k, date_from=from_day,date_until=until_day,filters={'categories':v})
        tmp = scraper.scrape()
#         print("scraper.scrape() outputs")
#         print(tmp)           
            
        if isinstance(tmp,list):
            for item in tmp:
                if item["id"] not in output:
                    output[item["id"]] = item
        time.sleep(30)
    #todo: sort output according to keys
    sorted_output = {}
    for id in sorted(output.keys(),reverse=True):
        sorted_output[id] = output[id]
    # sorted_output = {{k:output[k]} for k in sorted(output.keys(),reverse=True)}
    # sorted_output = sorted(output,reverse=True)

    base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
    cnt = 0

    for k,v in sorted_output.items():
        _id = v["id"]
        paper_title = " ".join(v["title"].split()).title()
        paper_url = v["url"]
        url = base_url + _id
        authors = ", ".join(v["authors"]).title()
        affiliation = v["affiliation"]
        abstract = v["abstract"].capitalize()
       
        print("id = ", _id," title = ", paper_title, " authors = ", authors)

        try:
            r = requests.get(url).json()
            if "official" in r and r["official"]:
                cnt += 1
                repo_url = r["official"]["url"]
                repo_name = repo_url.split("/")[-1]

                # content[_id] = f"|[{paper_title}]({paper_url})|[{repo_name}]({repo_url})|\n"
                content[_id] = f"|{paper_title}|{abstract}|{authors}|[{paper_url}]({paper_url})|[{repo_name}]({repo_url})|\n"
        except Exception as e:
            print(f"exception: {e} with id: {_id}")
    data = {DateToday:content}
    return data 

def update_daily_json(filename,data_all):
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
    
    #将datas更新到m中
    for data in data_all:
        m.update(data)

    # save data to daily.json
    with open(filename,"w") as f:
        json.dump(m,f)
    



def json_to_md(filename):
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
    # clean README.md if daily already exist else creat it
    with open("README.md","w+") as f:
        pass
    # write data into README.md
    with open("README.md","a+") as f:
        # 对data数据排序
        for day in sorted(data.keys(),reverse=True):
            day_content = data[day]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {day}\n")
            f.write("|Title|Abstract|Authors|PDFs|Code|\n" + "|---|---|---|---|---|\n")
            for item in day_content.items():
                
                k = item[0]
                v = item[1]
                if v is not None:
                    f.write(v)
    
    print("finished")        

if __name__ == "__main__":

    DateToday = datetime.date.today()
    N = 2 # 往前查询的天数
    data_all = []
    for i in range(1,N):
        day = str(DateToday + timedelta(-i))
        # you can add the categories in cats
        cats = {
        "cs":["cs.CV","cs.RO"]
#         "cs":["cs.CV","cs.RO","cs.AI","cs.MM"],
#         "eess":["eess.SP","eess.IV" ]
    }
        data = get_daily_code(day,cats)
        data_all.append(data)
    update_daily_json("cv-arxiv-daily.json",data_all)
    json_to_md("cv-arxiv-daily.json")
