#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/15/2017 5:16 PM
# @Author  : JZK
# @File    : main.py


from copy import deepcopy

#规定输入规则，模块名/函数名
url = input('Input URL:')

m,fun = url.split('/')

m = __import__('lib.' + m, fromlist= True)
#如果存在直接执行，否则404
if hasattr(m, fun):
    getattr(m, fun)()
else:
    print('404')