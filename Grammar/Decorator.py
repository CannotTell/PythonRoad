#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/2017 6:54 PM
# @Author  : JZK
# @File    : Decorator.py

'''
装饰器
'''

#最牛B的无视参数个数的
def niubi(func):
    def inner(*arg, **kwargs):
        print('before')
        ret = func(*arg, **kwargs)
        print('after')
        return ret
    return inner

#无参数装饰器
def outer(func):
    def inner():
        print('sb')
        ret = func()
        return ret
    return inner
@niubi
def index():
    print('xx')
    return True


#有参数装饰器
def hahah(func):
    def inner(a, b):
        print('before')
        ret = func(a,b)
        print('after')
        return ret
    return inner
@niubi
def second(a,b):
    print('a + b')
    return a + b




x = second(1,2)
index()
print(x)