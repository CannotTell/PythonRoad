#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2017 5:07 PM
# @Author  : JZK
# @File    : 进程通信.py

from multiprocessing import Pipe, Process, Queue
import os, time


# put到Queue里，这里put了2种类型的数据
def put_queue(queue, put_type, sleep_time):
    if put_type == 'int':
        for i in range(100):
            queue.put(i)
            print('{} PID PUT {}'.format(os.getpid(), i))
            time.sleep(sleep_time)
    elif put_type == 'str':
        for i in range(100):
            val = 'str{}'.format(i)
            queue.put(val)
            print('{} PID PUT {}'.format(os.getpid(), val))
            time.sleep(sleep_time)


# 一直获取queue里面的数据
def get_queue(queue):
    while True:
        info = queue.get()
        print('{} PID GET {}'.format(os.getpid(), info))


# 发送管道
def send_pipe(pipe):
    for i in range(1000):
        pipe.send(i)
        print('{} PID SEND {}'.format(os.getpid(), i))


# 接收管道
def receive_pipe(pipe):
    while True:
        ret = pipe.recv()
        if ret is not None:
            print('{} PID RECEIVE {}'.format(os.getpid(), ret))


def do_pipe():
    # The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way)
    rece_p, send_p = Pipe()
    p1 = Process(target=send_pipe, args=(send_p,))
    p2 = Process(target=receive_pipe, args=(rece_p,))

    p1.start()
    p2.start()

    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p1.join()
    p2.join()


def do_queue():
    queue = Queue(50)
    # 这里开2个进程放入数据，一个读取数据，因为Queue本身线程安全，无需担心共同访问资源问题
    p1 = Process(target=put_queue, args=(queue, 'str', 1,))
    p2 = Process(target=put_queue, args=(queue, 'int', 2,))
    p3 = Process(target=get_queue, args=(queue,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    do_queue()