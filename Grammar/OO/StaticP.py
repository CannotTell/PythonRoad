#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 2:14 PM
# @Author  : JZK
# @File    : StaticP.py

class Provice:
    #静态变量和静态方法存在类里
    #静态的方法和变量直接用类调用
    country = 'China'
    @staticmethod
    def f():
        print('fff')
    #类方法，和静态方法差不多，自动加入cls参数
    @classmethod
    def x(cls):
        print('x',cls)
    def __init__(self, name):
        self.name = name
        #self.start = 'init' 会报错
    def showName(self):
        print(self.name)
    #加入@Property后函数访问方式改变，不需要加（）调用，而且无法加参数
    @property
    def start(self):
        print('start...')
    #需要设置
    @start.setter
    def start(self, value):
        print(value)

shanghai = Provice('Shanghai')
zhejiang = Provice('Zhejiang')
shanghai.showName()
zhejiang.showName()

Provice.f()
Provice.x()
print(hasattr(shanghai, 'name'))
print(hasattr(shanghai, 'country'),id(shanghai.country))
print(id(shanghai))
print(id(zhejiang))
print(id(shanghai.country))
print(id(zhejiang.country))
shanghai.start