# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import datetime

url = 'http://dean.swjtu.edu.cn/servlet/NewsAction?Action=NewsMore'
res = requests.get(url)
# downfile.getWebPage(url)
soup = BeautifulSoup(res.text, 'lxml')


def getNdaysBefore(n):
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=n))
    # otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
    return otherStyleTime


def getNewsFromDean(interval):
    list_dean = []
    nodes = soup.find_all('li')

    if interval == '最近一天':
        n = 0
    elif interval == '最近三天':
        n = 3
    elif interval == '最近一周':
        n = 7
    else:
        n = 30

    getTime = getNdaysBefore(n)
    # getTime = '2017-09-30'
    for node in nodes:
        if len(node.contents) > 0 and node.contents[1].string >= getTime:
            info_new = {}
            info_new['source'] = '教务'
            info_new['path'] = 'http://dean.swjtu.edu.cn/servlet/NewsView?NewsID=' + node.contents[0].contents[0]['href'][27:]
            info_new['tag'] = '教务'
            info_new['title'] = node.contents[0].contents[0]['title']
            info_new['time'] = node.contents[1].string

            list_dean.append(info_new)

    return list_dean

# print (getNewsFromDean('最近一周'))
