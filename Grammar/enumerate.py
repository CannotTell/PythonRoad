#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 5:37 PM
# @Author  : JZK
# @File    : enumerate.py

#自动生产一列，默认从0开始，

li = ['apple', 'banana', 'candy']

for k, v in enumerate(li):
    print(k,v)

index = raw_input("Input:")
print(li[int(index)])