#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2017 10:49 AM
# @Author  : JZK
# @File    : PickleSaveO.py

import pickle

class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age


p = Person('Eirc',21)
#序列化
pickle.dump(p, open('save.log', 'wb'))
#反序列化
tp = pickle.load(open('save.log','rb'))
print(tp.Name)