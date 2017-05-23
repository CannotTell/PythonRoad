#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/18/2017 9:42 AM
# @Author  : JZK
# @File    : MultiplexingServer.py
import socket
import select

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 7000))
sk1.listen()

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 7001))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('127.0.0.1', 7002))
sk3.listen()

#将sock加入列表，然后select自动监听列表里的对象，一旦某个句柄发生变化
sk_list = [sk1, sk2, sk3]

while True:
    '''
    select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
    Wait until one or more file descriptors are ready for some kind of I/O.
    The first three arguments are sequences of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition''
    '''

    r_list, w_list, e_list = select.select(sk_list, [], sk_list, 1)
    for sk in r_list:
        conn, address = sk.accept()
        conn.sendall(bytes('How are you', encoding='utf-8'))
        print(conn)
        conn.close()