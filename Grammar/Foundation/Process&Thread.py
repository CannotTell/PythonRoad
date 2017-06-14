#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/2017 5:07 PM
# @Author  : JZK
# @File    : Process&Thread.py
# 多线程与多进程， IO密集型和CPU密集型
import multiprocessing
import time
import threading

#全局队列
Globa_Q = multiprocessing.Queue()
GLOBA_SEARCH_LIST = list(range(10000))

#队列初始化
def Init_queue():
    print('Init Queue...')
    #如果队列有值循环全部取出
    while not Globa_Q.empty():
        Globa_Q.get()
    #循环赋值
    for i in range(10):
        Globa_Q.put(i)
    print('Init Finished...')

def io_task(id):
    print('IO Task [%s] start' % id)
    while not Globa_Q.empty():
        time.sleep(1)#暂时挂起线程不占CPU资源
        try:
            data = Globa_Q.get(timeout=1)
            print('IO Task [%s] get data: %s' % (id, data))
        except Exception as ex:
            print('IO Task [%s] error: %s' % (id, str(ex)))
    print('IO Task[%s] end' % id)



def cpu_task(id):
    print('CPU Task %s Start...' % id)
    while not Globa_Q.empty():
        count = 0
        for i in range(10000):
            count = pow(2*3, 3*3) if i in GLOBA_SEARCH_LIST else 0
            try:
                data = Globa_Q.get(timeout=1)
                print('CPU Task %s get data %s' %(id,data))
            except Exception as ex:
                print('CPU Task %s Error: %s' %(id,str(ex)))
    print('CPU Task %s end' %id)

if __name__ == '__main__':
    print('CPU coutn: ', multiprocessing.cpu_count(), '\n')

    print('=======单线程IO密集型=======')
    Init_queue()
    start_time = time.time()
    io_task(0)
    print('End: ',time.time() -  start_time, '\n')


    print('=======多线程IO密集型========')
    Init_queue()
    start_time = time.time()
    thread_list = [threading.Thread(target=io_task, args=(i,)) for i in range(5)]
    for i in thread_list:
        i.start()
    for i in thread_list:
        if i.is_alive():
            i.join()
    print('End: ', time.time() - start_time, '\n')

    print('=======多进程IO密集型========')

    Init_queue()
    start_time = time.time()
    thread_list = [multiprocessing.Process(target=io_task, args=(i,)) for i in range(5)]
    for i in thread_list:
        i.start()
    for i in thread_list:
        if i.is_alive():
            i.join()
    print('End: ', time.time() - start_time, '\n')

    #https://zhuanlan.zhihu.com/p/24283040

    print("========== 直接执行CPU密集型任务 ==========")
    Init_queue()
    time_0 = time.time()
    cpu_task(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=cpu_task, args=(i,)) for i in range(5)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行cpu密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=cpu_task, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束：", time.time() - time_0, "\n")