#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 4:30 PM
# @Author  : JZK
# @File    : socker_server_Concurrent.py
'''
Socket真并发处理
select/epoll + socket + 多线程
'''
import socketserver
#必须继承socketserver.BaseRequestHandler，实现handle方法
class MySocket(socketserver.BaseRequestHandler):

    def handle(self):
        pass

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MySocket)
    server.serve_forever()