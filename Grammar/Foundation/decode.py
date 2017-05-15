#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 10:34 AM
# @Author  : JZK
# @File    : decode.py


# print("卧槽哦") 这样输出还是乱码

temp = "卧槽哦"    #utf-8

#解码是需要指定原来的编码
temp_unicode = temp.decode('utf-8')
temp_gbk = temp_unicode.encode('gbk')

print(temp_gbk)