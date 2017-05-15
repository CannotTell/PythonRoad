#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/14/2017 2:00 PM
# @Author  : JZK
# @File    : urlModule.py

from urllib import request      #发送http请求模块

f = request.urlopen('http://www.baidu.com')

result = f.read().decode('utf-8')
print(result)