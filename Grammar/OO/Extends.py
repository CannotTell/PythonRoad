#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 11:54 AM
# @Author  : JZK
# @File    : Extends.py

'''
支持多继承
如果多父类方法重名则按从左往右顺序继承
'''

class o1:
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
    def f(self):
        print('o1 f')

class o2:
    def f3(self):
        print('f3')
    def f4(self):
        print('f4')

    def f(self):
        print('o2 f')

class o (o1, o2):
    def f5(self):
        print('f5')

x = o()
x.f()

#复杂一点

class A:
    def f(self):
        print("A's f")
        self.f1()
class B(A):
    def f1(self):
        print("B's f1")
class C:
    def f1(self):
        print("C's f1")
class D(C, B):
    pass

o = D()
o.f()
