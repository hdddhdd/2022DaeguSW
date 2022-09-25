import os, re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "django_boilerplate.settings")
import django

django.setup()
from crawled_job.models import BoardData

page_num = 0

def fetch_job_latest_data():

    result = []

    #경영/사무/금융/보험 직종 - code=01
    #교육/법률/사회복지/경찰/소방 및 군인 - code=02
    #보건의료 - code=03
    #예술/디자인/방송/스포츠 - code=04
    #미용/여행/숙박/음식/경비/돌봄/청소 - code=05
    #영업/판매/운전/운송 - code=06
    #건설/채굴 - code=07
    #설치/정비/생산 - code=08

    for code in range(1, 9, 1):
        url= 'https://www.worktogether.or.kr/empInfo/empInfoSrch/list/retriveJobsCodeList.do?code=0' + str(code) + '&depth=2'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        web_page_link_root = "https://www.worktogether.or.kr"
        #next_page_url = soup.find("div", "paging").find_all("a")
        #print(len(next_page_url))

        table = soup.find("table", {"class":"board_list"})
        tbody = table.find("tbody")
        list_items = tbody.find_all("tr")

        #job_field
        field = code

        for item in list_items:
            # link
            page_link_raw = item.find("td", "title").find("a")["href"]
            normalized_page_link = web_page_link_root + "/" + page_link_raw
            page_link_parts = urlparse(normalized_page_link)

            #company
            company = item.find("td", "title").find("a").get_text()

            #title
            title = item.find("p", "link")["title"]

            #salary_type
            salary_type = item.find("span").find("img")["alt"]


            detail_info = item.find("p", "board_list_info").find_all("span")
            #print(detail_info)

            emp = []
            for info in detail_info: 
                text_raw = info.get_text()
                text = re.sub(r"[\n\t]*", "", text_raw)
                emp.append(text)
            # print('\n')
            # print(emp[0])
            # print(emp[1])
            # print(emp[2])
            # print('\n')
            # print('\n')
            # print('\n')

            item_obj = {
                'field': field,
                'link': normalized_page_link,
                'title': title,
                'company': company,
                'salary_type': salary_type,
                'salary': emp[0],
                'regular': emp[1],
                'detail': emp[2]
            }

            result.append(item_obj)
            #print(len(result))

    return result

def add_new_items(crawled_items):
    last_inserted_items = BoardData.objects.last()

    items_to_insert_into_db = []

    for item in crawled_items:
        items_to_insert_into_db.append(item)
    items_to_insert_into_db.reverse()

    #print(len(items_to_insert_into_db))
    for item in items_to_insert_into_db:
        #print("new item added!! : " + item['job_field'] + item['company'] + item['title'] + item['salary_type'])

        BoardData(
                  field=item['field'],
                  company=item['company'],
                  title=item['title'],
                  salary_type=item['salary_type'],
                  salary=item['salary'],
                  regular=item['regular'],
                  detail=item['detail'],
                  link=item['link']).save()

    return items_to_insert_into_db

if __name__ == '__main__':
    #fetch_job_latest_data()
    add_new_items(fetch_job_latest_data())