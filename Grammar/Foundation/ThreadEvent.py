#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/26/2017 10:37 AM
# @Author  : JZK
# @File    : ThreadEvent.py
import threading

def do(event):
    print('start')
    event.wait()
    print('execute')

event_object = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_object,))
    t.start()
event_object.clear()
inp = input('input:')
if inp == 'true':
    event_object.set()