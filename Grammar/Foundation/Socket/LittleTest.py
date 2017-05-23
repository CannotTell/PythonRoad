#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/18/2017 1:44 PM
# @Author  : JZK
# @File    : LittleTest.py

b = bytes('hello ',encoding='utf-8') + bytes('You', encoding='utf-8')
print(str(b,encoding='utf-8'))