#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/2017 11:35 AM
# @Author  : JZK
# @File    : TestMemory.py

a1 = -5
a2 = -5

print(id(a1))
print(id(a2))
print(a1 is a2)

while (a1 is a2):
    a1 += 1
    a2 += 1

print(a1)
print(a2)