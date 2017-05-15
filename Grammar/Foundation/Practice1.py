#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 6:30 PM
# @Author  : JZK
# @File    : Practice1.py

#查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

sum = []
sum.extend(li)
sum.extend(tu)
sum.extend(dic.values())

for item in sum:
    tempStr = str(item).strip().capitalize()
    if tempStr[0:1] == 'A' and tempStr[-1] == 'c':
        print(item)
    else:
        #print('xxx')
        continue

#print(sum)