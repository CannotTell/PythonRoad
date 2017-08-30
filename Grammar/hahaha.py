#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/2/2017 12:10 PM
# @Author  : JZK
# @File    : hahaha.py

# import time
#
# start = time.time()
# time.sleep(3)
# stop = time.time()
#
# print(stop - start)

# with open('shadowsocks.log','r') as file1, open('NewShadowsocks.log','w')as file2:
#
#             for line in file1:
#                 try:
#                     if 'INFO' in line:
#                         file2.write(line)
#                 except Exception as e:
#                     print(e)
#                     continue

old_file = open('shadowsocks.log','r')
new_file = open('NewShadowsocks.log','w')

while True:
    try:
        line = old_file.readline()
        if 'INFO' in line:
            new_file.write(line)
        if not line:
            break
    except Exception as e:
        print(e)
        continue

old_file.close()
new_file.close()
print('Finish')