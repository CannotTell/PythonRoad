#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午9:08
# @Author  : JZK
# @File    : Condition金拱门和我.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

from threading import Thread, Condition
from queue import Queue
import time
import random


def jingongmeng(que, con):
    i = 1
    # 确保我先提需求
    while True:
        # 获得锁
        con.acquire()
        # 等待客户订单
        con.wait()
        print('生产汉堡{}'.format(i))
        time.sleep(1)
        que.put(i)
        print('通知我汉堡{}已完成'.format(i))
        con.notify()
        i += random.randint(1, 5)
        # 释放锁
        con.release()


def wo(que, con):
    # 确保金拱门先进入等待状态
    time.sleep(2)
    for i in range(10):
        # 获得锁
        con.acquire()
        # 通知金拱门要汉堡
        con.notify()
        print('需要一个汉堡!')
        # 等出汉堡
        con.wait()
        print('拿到一个汉堡{}'.format(que.get()))
        con.release()
    print('饱了！')


if __name__ == '__main__':
    q = Queue(5)
    con = Condition()
    t1 = Thread(target=jingongmeng, args=(q, con,))
    t2 = Thread(target=wo, args=(q, con,))

    t1.setDaemon(True)
    t1.start()

    t2.start()

    t2.join()
    print('finished')
