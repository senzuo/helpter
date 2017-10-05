# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import util



def getDefult():
    url = 'http://yanghua.swjtu.edu.cn/WebSite/Head/AcademyBulletin.aspx?CollegeNo='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    preUrl = 'http://yanghua.swjtu.edu.cn/WebSite/Head/'
    list_yang = []
    div = soup.find_all(id='Content')[0]
    for row in div.contents[0].contents:
        info_new = {}
        info_new['source'] = '扬华'
        info_new['path'] = preUrl + row.contents[1].contents[0]['href']
        info_new['title'] = row.contents[1].text[0:-12]
        info_new['tag'] = util.getTag(info_new['title'])
        info_new['time'] = row.contents[1].text[-11:-1]
        list_yang.append(info_new)
    return list_yang

    # print (getDefult())
