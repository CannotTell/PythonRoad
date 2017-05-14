#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/12/2017 9:28 AM
# @Author  : JZK
# @File    : sysModule.py


import sys

sys.argv           #命令行参数List，第一个元素是程序本身路径
sys.exit(0)        #退出程序，正常退出时exit(0)
sys.version        #获取Python解释程序的版本信息
sys.maxint        # 最大的Int值
sys.path          # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
