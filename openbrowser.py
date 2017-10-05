#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import sys
import webbrowser
sys.path.append("libs")

 
def openbrowser(url):
	# url = 'http://www.baidu.com'
	webbrowser.open(url)