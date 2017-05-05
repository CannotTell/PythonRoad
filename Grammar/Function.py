#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/2017 2:04 PM
# @Author  : JZK
# @File    : Function.py

#动态参数
def f(*a):  #默认类型为元组
    print(a, type(a))

def f2(**a): #默认为字典类型
    print(a, type(a))
#t = (1,2,3)
f2(k=1,x=2,y=3,z=4)


