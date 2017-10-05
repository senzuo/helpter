# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import util
import datetime

url1 = 'http://sist.swjtu.edu.cn/list.do?action=news&navId=37'
url2 = 'http://sist.swjtu.edu.cn/list.do?action=news&navId=38'
url3 = 'http://sist.swjtu.edu.cn/list.do?action=news&navId=46'
url4 = 'http://sist.swjtu.edu.cn/list.do?action=news&navId=77'
url5 = 'http://sist.swjtu.edu.cn/list.do?action=news&navId=51'
urls = [url1, url2, url3, url4, url5]


def getNdaysBefore(n):
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=n))
    # otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
    return otherStyleTime


def getInfo(interval):
    list_college_info = []
    if interval == '最近一天':
        n = 0
    elif interval == '最近三天':
        n = 3
    elif interval == '最近一周':
        n = 7
    else:
        n = 30

    getTime = getNdaysBefore(n)
    for url in urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        for new in soup.dl.contents:
            if len(new) > 1 and getTime <= new.contents[1].string:
                info_new = {}
                info_new['source'] = '信息学院'
                info_new['path'] = new.contents[0].contents[1]['href']
                info_new['title'] = new.contents[0].contents[1]['title']
                info_new['tag'] = util.getTag(info_new['title'])
                info_new['time'] = new.contents[1].string
                list_college_info.append(info_new)
                pass
    return list_college_info

# print (getInfo('最近一周'))
