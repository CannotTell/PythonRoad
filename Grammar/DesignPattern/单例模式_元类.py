#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/2017 1:42 PM
# @Author  : JZK
# @File    : 单例模式_元类.py


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(self, *args, **kwargs):