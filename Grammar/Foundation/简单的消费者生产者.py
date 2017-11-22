#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午3:54
# @Author  : JZK
# @File    : 简单的消费者生产者.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
from threading import Thread
from queue import Queue
import time


def producer(put_que):
    i = 1
    while True:
        print('put a {}'.format(i))
        put_que.put(i)
        time.sleep(2)
        i += 1


def consumer(get_que):
    while True:
        print('get a {}'.format(get_que.get()))
        time.sleep(1)


if __name__ == '__main__':
    q = Queue(10)

    t1 = Thread(target=producer, args=(q,))
    t2 = Thread(target=consumer, args=(q,))

    # 设置主线程结束，子线程也结束
    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()

    start_time = time.time()

    while True:
        if (time.time() - start_time) < 30:
            continue
        print(t1.is_alive())
        print(t2.is_alive())
        break
    print('finished...')