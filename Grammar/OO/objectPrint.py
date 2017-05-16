#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 5:44 PM
# @Author  : JZK
# @File    : objectPrint.py
'''
类似于Java里的重写toString
'''
class A:
    def __init__(self):
        print('Create A')
        self.__Name = 'A'
    def __str__(self):
        return self.__Name

class B:
    def __init__(self):
        print('Create B')

a = A()
b = B()
print(a)
print(b)