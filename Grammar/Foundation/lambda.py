#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/2017 11:21 PM
# @Author  : JZK
# @File    : lambda.py

#简单的函数可以用Lambda表达式表达

def f1():
    return 1
f2 = lambda : 1
print(f1())
print(f2()) #f1和f2一样

def f3(a1,a2):
    return a1 + a2
f4 = lambda a1, a2 : a1 + a2

print(f3(1,2))
print(f4(3,4))  #f3和f4一样