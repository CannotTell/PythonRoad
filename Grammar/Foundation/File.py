#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/7/2017 11:16 AM
# @Author  : JZK
# @File    : File.py

#open（文件名，模式，编码）

'''
r ，只读模式【默认】
w，只写模式【不可读；不存在则创建；存在则清空内容；】
x， 只写模式【不可读；不存在则创建，存在则报错】
a， 追加模式【可读；   不存在则创建；存在则只追加内容；】

带b都是以字节的方式打开文件
rb  或 r+b
wb 或 w+b
xb 或 w+b
ab 或 a+b

Python底部以字节为基本打开文件，当我们已基本方式打开文件时， Python将字节自动处理为字符串打开
'''

FilePath = 'C:\\Users\\zhukai.jiang\\PycharmProjects\\PythonRoad\\Files\\TestFile.txt'

#默认是只读模式和以字符串的方式打开
f = open(FilePath,'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

#以字节形势打开文件
f = open(FilePath,'rb')
data = f.read()
f.close()
print(data)

'''
    + 表示可以同时读写某个文件
    
    r+， 读写【可读，可写】
    w+，写读【可读，可写】
    x+ ，写读【可读，可写】
    a+， 写读【可读，可写】
'''

#r+ 读取文件看指针位置
# 写文件都在是从文件最后追加,指针移到文件最后
f = open(FilePath, 'r+', encoding='utf-8')
data = f.read()
print(type(data),data)

f.write('Test Write')
print(f.tell())#获取当前指针位置
f.seek(0)#将指正调整到文件头
data = f.read()
print(type(data),data)

f.close()

#w+
#默认打开文件后清空文件里的内容
#x和w一样，只有当打开文件不存在是x会报错
f = open(FilePath, 'w+', encoding='utf-8')
data = f.read()
print(type(data),data)

f.write('Test Write')
f.seek(0)#将指正调整到文件头
data = f.read()
print(type(data),data)

f.close()

#a+
#默认打开文件指真到文件最后
f = open(FilePath, 'a+', encoding='utf-8')
data = f.read()
print(type(data),data)

f.write('Test Write')
f.seek(0)#将指正调整到文件头
data = f.read()
print(type(data),data)

f.close()

#用with as语句 Python自动关闭文件，不需要写close
#Python2.7之后支持同事打开2个文件
with open(FilePath,'r') as f:
    f.read()
#同时打开2个文件copy
with open('SourceFile','r') as file1, open('NewFile','w')as file2:
    for line in file1:
        file2.write(line)
