#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2017 5:12 PM
# @Author  : JZK
# @File    : dict.py

#字典的元素，键值对

user_info = {
    'name' : 'Eric',
    'age' : 18,
    'gender' : 'M',
    'money' : 'rich'
}

#索引
print(user_info['name'])

#循环 默认输出Key
for item in user_info:
    print(item)
    print(user_info[item])

#取所有的值、Value和键值对
print(user_info.keys())
print(user_info.values())
print(user_info.items())

for item in user_info.values():
    print(item)
for k, v in user_info.items():
    print(k)
    print(v)

#get 根据Key获取Value，如果不存在，返回一个默认值
print(user_info.get('age'))
print(user_info.get('xxx'))
print(user_info.get('xxx',-1))

#删除
del user_info['money']
print(user_info)
#清除所有内容
user_info.clear()
print(user_info)