#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/17/2017 10:06 AM
# @Author  : JZK
# @File    : main.py

import BaseClass as bc
import random

tec1 = bc.Teacher('Eric', 'M', 21)
tec2 = bc.Teacher('老王', 'F', 22)

st1 = bc.Student('A', 'M', 10)
st2 = bc.Student('B', 'F', 10)
st3 = bc.Student('C', 'FM', 10)

Course_Lists = []

for i in range(0,4):
    t = tec1
    x = random.randrange(0,2)
    if x == 0:
        t = tec2
    Course_Lists.append(bc.Course(bc.Course.totalClass[i], random.randrange(1,10), t, random.randrange(1,4)))

for y in Course_Lists:
    print(y.COURSE_NAME, y.COURSE_TEACHER, y.COURSE_TIME, y.COURSE_PRICE)

#随机选课
