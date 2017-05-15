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


r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G7558&UserID=')
result = r.text

# 解析XML格式内容
root = ET.XML(result)
for node in root.iter('TrainDetailInfo'):
    print(node.find('TrainStation').text,node.find('StartTime').text,node.tag,node.attrib)