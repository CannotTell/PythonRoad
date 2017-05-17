#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 12:19 PM
# @Author  : JZK
# @File    : Socker_Server.py

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen(5)

while True:
    conn, address = sk.accept() #线程阻塞
    print(address,conn)
    conn.sendall(bytes('Have a good day!', encoding='utf-8'))

    while True:
        ret = conn.recv(1024) #接受字节大小
        ret_str = str(ret, encoding='utf-8')
        if ret_str == 'q' or ret_str == 'Q':
            break
        conn.sendall(bytes(ret_str + '_From Server', encoding='utf-8'))
