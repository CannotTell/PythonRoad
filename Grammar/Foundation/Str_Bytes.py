#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/3/2017 3:10 PM
# @Author  : JZK
# @File    : Str_Bytes.py


s1 = '撒打算'
s2 = '上大'

#字符转字节

b1 = bytes(s1, encoding='utf-8')
print(b1)
b2 = bytes(s2, encoding='gbk')
print(b2)

#将字节转换为字符
news1 = str(b1, encoding='utf-8')
print(news1)
news2 = str(b2,encoding='gbk')
print(news2)