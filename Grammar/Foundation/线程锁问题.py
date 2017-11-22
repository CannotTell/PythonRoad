#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午3:00
# @Author  : JZK
# @File    : 线程锁问题.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

import threading
"""
理论上这个total的值应该始终是0
"""
# 全局变量初始为0
total = 0
# 创建锁
lock = threading.Lock()


def change_total(n):
    global total
    total += n
    total -= n


def run_times(n):
    # 获取锁
    lock.acquire()
    try:
        for i in range(1000000):
            change_total(n)
    finally:
        # 释放锁
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=run_times, args=(8,))
    t2 = threading.Thread(target=run_times, args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(total)