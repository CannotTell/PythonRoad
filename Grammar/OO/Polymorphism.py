#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 12:15 PM
# @Author  : JZK
# @File    : Polymorphism.py
'''
python的动态语言特性可以很好的多态
'''



class o1():
    def __init__(self):
        self.a = "o1's a"
    def f(self):
        print("o1's f")


class o2():
    def __init__(self):
        self.a = "o2's a"
    def f(self):
        print("o2's f")



def output(arg):
    arg.f()
    print(arg.a)


output(o1())
output(o2())


