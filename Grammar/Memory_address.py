#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/3/2017 11:51 AM
# @Author  : JZK
# @File    : Memory_address.py

a1 = 12
a2 = 12
a3 = 123

print(id(a1))
print(id(a2))
print(a1 is a2)
print(id(a3))


name = str('我哈')

for item in name:
    #print(item)
    byteList = bytes(item, encoding='utf-8')
    #print(byteList)
    for i in byteList:
        print(i)
        print(bin(i))