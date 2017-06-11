#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/11/2017 12:47 PM
# @Author  : JZK
# @File    : ProcessData.py
# 多进程不共享数据

from multiprocessing import Process
from threading import Thread


li = []

def foo(i):
    li.append(i)
    print('Hello ', li)

if __name__ == '__main__':
    for i in range(10):
        #p = Process(target=foo, args=(i,))  # 进程
        p = Thread(target=foo, args=(i,))   #线程
        p.start()