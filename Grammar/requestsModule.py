#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/14/2017 3:40 PM
# @Author  : JZK
# @File    : requestsModule.py

import requests

#第三方模块 pip install requests,爬虫

response = requests.get('http://www.weather.com.cn/adat/sk/101020100.html')
response.encoding = 'utf-8'
result = response.text
print(type(result),result)


response = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=1483687801')
response.encoding = 'utf-8'
result = response.text
print(result)

from xml.etree import ElementTree as ET

node = ET.XML(result)
print(node.text)
