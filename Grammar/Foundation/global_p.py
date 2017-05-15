#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/2017 2:25 PM
# @Author  : JZK
# @File    : global_p.py

NAME = 'ERIC'   #全局变量

#方法内无法修改全局变量，除非加上关键字 global
def f():
    global NAME
    print(NAME)
    NAME = 'xxxx'

print(NAME)
f()
print(NAME)