#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/2017 2:56 PM
# @Author  : JZK
# @File    : Recursion.py

#递归，最典型的斐波那契数列
#F[n]=F[n-1]+F[n-2](n>=2,F[0]=0,F[1]=1)

def Fibonacci(num):
    '''
    斐波那契数列递归算法
    :param num: 
    :return: 
    '''
    if(num == 1 or num == 0):
        print(num)
    else:
        print(Fibonacci(num - 1) + Fibonacci(num - 2))


def FibonacciNoRec(num):
    li = [1] * num
    li[0] = 1
    for i in range(2,num):
        li[i] = li[i - 1] + li[i - 2]

    return li

print(FibonacciNoRec(6))