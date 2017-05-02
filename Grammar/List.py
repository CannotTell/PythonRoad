#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 4:45 PM
# @Author  : JZK
# @File    : List.py

#元组和List功能几乎一样，但是元组是不能修改的

name_list = ['eric', 'Tom', 'Iris']

#索引
print(name_list[0])

#切片
print(name_list[0:2])

#len
print(name_list[1:len(name_list)])

#for
for item in name_list:
    print(item)

#向后追加
name_list.append('xx')
name_list.append('xx')
print(name_list)
#元素出现的次数
print(name_list.count('xx'))
#扩展，批量添加
new_list = ['1','2','3']
name_list.extend(new_list)
print(name_list)
#获取指定元素索引
print(name_list.index('xx'))
#向指定位置插入
name_list.insert(3,'yy')
print(name_list)
#弹出最后一个值
x = name_list.pop()
print(x)
print(name_list)
#移除某个元素一次
name_list.remove('xx')
print(name_list)
#删除特定位置值
del name_list[1]
print(name_list)
del name_list[0:6]
print(name_list)