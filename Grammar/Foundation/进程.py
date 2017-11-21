#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2017 3:24 PM
# @Author  : JZK
# @File    : 进程.py
import multiprocessing
import time


def do_something(time_sleep, process_name):
    print('hello, My Process Name is {}'.format(process_name))
    time.sleep(time_sleep)


# 单进程
def single_process():
    p = multiprocessing.Process(target=do_something, args=(1, 'process NO.1'))
    p.start()
    print('process id:{}; process Name:{}; process is alive:{}'.format(p.pid, p.name, p.is_alive()))


# 多进程
def multi_progress():
    for i in range(4):
        p = multiprocessing.Process(target=do_something, args=(1, 'process NO.{}'.format(i)))
        p.start()
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for j in multiprocessing.active_children():
        print("child p.name:{}; p.id:{}; p.is_alive:{}".format(j.name, j.pid, j.is_alive()))
    print("END!!!!!!!!!!!!!!!!!")


if __name__ == '__main__':
    #single_process()
    multi_progress()