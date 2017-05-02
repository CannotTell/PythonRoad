#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 11:56 AM
# @Author  : JZK
# @File    : Check_API.py

#查看类的函数和API的函数和方法

# 查看类的方法
string = 'xxx'
print(dir(string))

integer = 3
print(dir(integer))

#str
li = ['xy','ab','sh']
print('_'.join(li))

#去左右两边空格，中间不管
s = ' xyz '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

