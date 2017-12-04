#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/4/2017 3:53 PM
# @Author  : JZK
# @File    : 排序算法.py


# 冒泡排序
def bubble_sort(arr_list):
    for i in range(len(arr_list) - 1):
        for j in range(len(arr_list) - 1 - i):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
    return arr_list


# 选择排序（寻找最小值与第一个交换位置）和冒泡有点类似
def select_sort(arr_list):
    for i in range(len(arr_list) - 1):
        # 默认最小值得index位置
        min_index = i
        for j in range(i, len(arr_list)):
            if arr_list[j] < arr_list[min_index]:
                min_index = j
        arr_list[i], arr_list[min_index] = arr_list[min_index], arr_list[i]
    return arr_list


# 打扑克抓牌过程是典型的插入算法
def insert_sort(arr_list):
    for i in range(len(arr_list)-1):
        for j in range(i+1):
            if arr_list[i+1] < arr_list[i]:
                arr_list[i], arr_list[i+1] = arr_list[i+1], arr_list[i]
            i -= 1

    return arr_list


if __name__ == '__main__':
    li = [123, 4, 5, 2, 234, 5, 64, 76, 2, 4, 56, 23, 4, 4, 6, 3, 5, 3, 32, 6, 655, 634, 5, 34]
    print(insert_sort(li))
