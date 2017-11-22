#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午2:41
# @Author  : JZK
# @File    : 多线程.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
import threading
import time


def test_thread():
    thread_name = threading.current_thread().name
    print('Thread {} is running...'.format(thread_name))
    for i in range(3):
        print('Thread {} is print {}'.format(thread_name, i))
        time.sleep(1)
    print('thread {} is end'.format(thread_name))


if __name__ == '__main__':
    print('thread {} is start...'.format(threading.current_thread().name))
    t1 = threading.Thread(target=test_thread, name='test_thread1')
    t2 = threading.Thread(target=test_thread, name='test_thread2')

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('thread {} is finished'.format(threading.current_thread().name))