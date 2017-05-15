#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/3/2017 3:29 PM
# @Author  : JZK
# @File    : ListTranfer.py

s1 = '打卡的文件建安费'
l1 = list(s1)
print(l1)

t1 = ('asd', '撒旦','asdadaw')
l1 = list(t1)
print(l1)

d = {'1': '收款单', '2':'sda','ss':'adwdcfa'}
l1 = list(d.items())
print(l1)


t2 = ('说到底',23,{'k1':1})   #元组不可修改
print(t2)
t2[2]['k2'] = 3 #Or t2[2].update({'k2':123})
print(t2)


dic = {'k1':1, 'k2':2, 'k3':3}
print(dic)
dic['k1'] = 5
print(dic)

n = dict.fromkeys(['k1','k2','k3'],'x')
print(n)
n['k1'] = 'xx'
print(n)

n2 = dict.fromkeys(['k1','k2','k3'],[])
print(n2)
n2['k1'].append('xx')
print(n2)