#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/14/2017 1:09 PM
# @Author  : JZK
# @File    : ModuleDetail.py

print(__doc__)      #py文件的注释
print(__file__)     #本身自己文件的路径
print(__package__)  #当前包
print(__cached__)   #当前缓存文件 py3中有
print(__name__)     #如果是执行文件为__main__，如果为引入文件则为文件名函数
                    #主文件调用主函数时，必须加判断