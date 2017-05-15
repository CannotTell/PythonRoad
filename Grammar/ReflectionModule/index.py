#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/15/2017 4:36 PM
# @Author  : JZK
# @File    : index.py

'''
通过名字来导入模块
'''

inp = input('输入模块：')

m = __import__(inp)
#__import__('jzk.test.com', fromlist = True)需要加上参数才能导路径
funName = 'f1'
print(dir(m))
f = getattr(m,funName)
#提取m模块里的funName函数,可以获取函数，也可以获取变量
#hasattr判断是否存在

print(f())
#print(m.getattr())