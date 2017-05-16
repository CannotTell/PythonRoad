#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 3:53 PM
# @Author  : JZK
# @File    : CallMethod.py

class o:
    #init只允许返回None
    def __init__(self):
        return None
    #call方法是对象（）后执行
    def __call__(self, *args, **kwargs):
        return 1
    def __getitem__(self, item):
        return 2
    def __setitem__(self, key, value):
        return 3
O = o()
print(o(),type(o()))
print(o()(),type(o()()))
print(o()[''],type(o()['']))
#print((o()[] = 1))
print(o.__dict__)
print(O.__dict__)