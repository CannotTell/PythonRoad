#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午5:46
# @Author  : JZK
# @File    : 金拱门和我.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
"""
用Event来唤醒线程
注意Event能唤醒所有挂起的线程，如果想要唤醒指定的线程还得用Semaphore和Condition
"""
from threading import Thread, Event
from queue import Queue
import time
import random


def jingongmeng(que, ev):
    i = 1
    while True:
        # 等待需求通知
        ev.wait()
        print('生产汉堡{}'.format(i))
        que.put(i)
        i += random.randint(1, 5)
        # 生产完后就停工
        ev.clear()


def wo(que, ev):
    for i in range(10):
        # 通知需要汉堡
        ev.set()
        print('需要一个汉堡!')
        print('拿到一个汉堡{}'.format(que.get()))

        sleep_time = random.randrange(2, 5)
        print('随机等待{}秒'.format(sleep_time))
        time.sleep(sleep_time)
    print('饱了！')


if __name__ == '__main__':
    q = Queue(5)
    ev = Event()
    t1 = Thread(target=jingongmeng, args=(q, ev,))
    t2 = Thread(target=wo, args=(q, ev,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('finished')

