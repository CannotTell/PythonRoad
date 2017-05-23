#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/18/2017 12:00 PM
# @Author  : JZK
# @File    : fakeUsersConnect.py
'''
模拟多个客户端连接一个socket服务并发送消息
伪并发
用Python里的select 和 socket的模块实现伪并发
r_list:读写一起
w_list：读写分离
'''
import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1', 7000))
sk.listen()
Lists = [sk]
outputs = []
message_dict = {}

while True:
    #如果有人第一次连接sk，则sk发送变化
    #这里select监听2种对象
    r_list, w_list, e_list = select.select(Lists, outputs, Lists, 1)
    print('listening Object %d' %len(Lists))
    for i in r_list:
        if i == sk:
            #表示有新用户来连接了
            #每个连接对象，Lists里放了2种数据，socket服务端和socket客户端
            conn, address = i.accept()
            Lists.append(conn)
            message_dict[conn] = []
        else:
            #有老用户发消息了
            try:
                data = k.recv(1024)
            except Exception as ex:
                Lists.remove(i)
            else:
                #k.sendall(bytes('Received ', encoding='utf-8') + data)
                message_dict[i].append(data)
                outputs.append(i)

    for j in w_list:
        rece_data = message_dict[j][0]
        del message_dict[j][0]
        j.sendall(bytes('Received ', encoding='utf-8') + rece_data)
        outputs.remove(j)

    for k in e_list:
        Lists.remove(k)
