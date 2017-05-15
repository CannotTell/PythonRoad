#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/15/2017 2:22 PM
# @Author  : JZK
# @File    : configparserModule.py

import configparser
'''
configparser用于处理特定格式的文件，其本质上是利用open来操作文件。
格式如下
[section1] # 节点
k1 = v1    # 值
k2:v2       # 值
 
[section2] # 节点
k1 = v1    # 值
'''

#获取所有节点

config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
ret = config.sections()
print(ret)
#获取指定节点下所有的键值对
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
ret = config.items('section1')
print(ret)
#获取指定节点下所有的建
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
ret = config.options('section1')
print(ret)
#获取指定节点下指定key的值
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
v = config.get('section1', 'k1')
# v = config.getint('section1', 'k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')

print(v)
#检查、删除、添加节点
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')

# 检查
has_sec = config.has_section('section1')
print(has_sec)

# 添加节点
config.add_section("SEC_1")
config.write(open('xxxooo', 'w'))

# 删除节点
config.remove_section("SEC_1")
config.write(open('xxxooo', 'w'))
#检查、删除、设置指定组内的键值对
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')

# 检查
has_opt = config.has_option('section1', 'k1')
print(has_opt)

# 删除
config.remove_option('section1', 'k1')
config.write(open('xxxooo', 'w'))

# 设置
config.set('section1', 'k10', "123")
config.write(open('xxxooo', 'w'))