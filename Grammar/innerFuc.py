#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/6/2017 11:54 AM
# @Author  : JZK
# @File    : innerFuc.py

#绝对值
print(abs(-111))

#all循环参数，如果每个参数都为真，那么all的返回值为真
print(all([True, True, True,]))
#any只要有一个为真，就为真
print(any([True,False]))
#假的参数 0, None, 空的都是假的
print(bool(0),bool(1),bool(-1),bool(None),bool('ss'),bool(''))

#ascii()，对象类中找__repr__，获取其返回值
class food:
    def __repr__(self):
        return 'test ascii'
f = food()
print(ascii(f))

'''
bin()二进制
oct()八进制
int()十进制
hex()十六进制
'''
print(bin(10))
print(oct(10))
print(int(10))
print(hex(10))

#生产随机数
#数字转字母 chr（数字） 65-90 ascii
import random

temp = ''
for i in range(4):
    randomNum = random.randrange(0,3)
    if randomNum == 0:
        c = chr(random.randrange(65, 91))
        temp += c
    else:
        temp += str(random.randrange(0,10))

print(temp)

#ord和chr
print(chr(65))
print(ord('A'))

#divmod 分页可以用
print(10/3)
print(divmod(10,3))

#eval转换表达式并计算 有返回值
#exec执行代码 无返回值
s = '1 + 3 * 8'
print(eval(s))
# filter筛选

def x(i):
    if i > 10:
        return True
    else:
        return False

li = [10,11,9,20]
li = filter(x,li)
print(type(li))
for item in li:
    print(item)

s1 = ['1','213','124113','fe','sdfqd','aw43s','1qasa','十三五']
s1 = sorted(s1)
print(s1)