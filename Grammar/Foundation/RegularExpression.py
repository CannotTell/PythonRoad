#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/9/2017 10:51 AM
# @Author  : JZK
# @File    : RegularExpression.py

import re
'''
字符：

 

　　. 匹配除换行符以外的任意字符
　　\w	匹配字母或数字或下划线或汉字
　　\s	匹配任意的空白符
　　\d	匹配数字
　　\b	匹配单词的开始或结束
　　^	匹配字符串的开始
　　$	匹配字符串的结束

 

次数：

 

　　* 重复零次或更多次
　　+	重复一次或更多次
　　?	重复零次或一次
　　{n}	重复n次
　　{n,}	重复n次或更多次
　　{n,m}	重复n到m次
'''

origin = 'hello world jsdad awdujx askd '
# match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
#无分组

r = re.match('h\w+', origin)
print(r.group()) #获取匹配到的所有结果
# 为何要有分组？提取匹配成功的指定内容（先匹配成功全部正则，再匹配成功的局部内容提取出来）
#分组
r1 = re.match('(h)(\w+)', origin)
r2 = re.match('(?P<k1>h)(?P<k2>\w+)', origin)

print(r1.groups()) #获取匹配到的分组结果
print(r2.groupdict()) #获取匹配到的分组结果

# search,浏览整个字符串去匹配第一个，未匹配成功返回None

#无分组

r = re.search('h\w+', origin)
print(r.group()) #获取匹配到的所有结果

#分组
r1 = re.search('(h)(\w+)', origin)
r2 = re.search('(?P<k1>h)(?P<k2>\w+)', origin)

print(r1.groups()) #获取匹配到的分组结果
print(r2.groupdict()) #获取匹配到的分组结果

# findall，获取非重复的匹配列表；如果有一个组则以列表形式返回，且每一个匹配均是字符串；如果模型中有多个组，则以列表形式返回，且每一个匹配均是元祖；
# 空的匹配也会包含在结果中

# 无分组
r = re.findall("a\w+",origin)
print(r)

# 有分组
origin = "hello alex bcd abcd lge acd 19"
r = re.findall("a((\w*)c)(d)", origin)
print(r)


# sub，替换匹配成功的指定位置字符串
origin = "hello alex bcd alex lge alex acd 19"
r = re.sub("a\w+", "999", origin, 2)
print(r)

# split，根据正则匹配分割字符串

# 无分组
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("alex", origin, 1)
print(r)

# 有分组

origin = "hello alex bcd alex lge alex acd 19"
r1 = re.split("(alex)", origin, 1)
print(r1)
r2 = re.split("(al(ex))", origin, 1)
print(r2)