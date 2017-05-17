#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 8:31 AM
# @Author  : JZK
# @File    : ConnectionPool.py

'''
单例模式
'''
import random

class ConnectionPool:

    __instance = None

    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            ConnectionPool.__instance = ConnectionPool()
            return ConnectionPool.__instance

    def __init__(self):
        self.IP = 'ip'
        self.PORT = 'port'
        self.PWD = 'pwd'
        self.USERNAME = 'username'

        self.connList = [1,2,3,4,5,6,7,8,9,10]

    def getConnection(self):
        #随机返回一个连接
        r = random.randrange(0,10)
        return self.connList[r]


obj1 = ConnectionPool.get_instance()
print(obj1)
obj2 = ConnectionPool.get_instance()
print(obj2)
obj3 = ConnectionPool.get_instance()
print(obj3)