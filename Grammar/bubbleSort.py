#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/2017 2:15 PM
# @Author  : JZK
# @File    : bubbleSort.py



def bubbleSort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j+1] = li[j+1],li[j]
    return li

li = [123,4,5,2,234,5,64,76,2,4,56,23,4,4,6,3,5,3,32,6,655,634,5,34,]

print(bubbleSort(li))