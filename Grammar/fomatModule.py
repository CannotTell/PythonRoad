#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/14/2017 12:45 PM
# @Author  : JZK
# @File    : fomatModule.py

tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')
print(tpl)
tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
print(tpl)
tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
print(tpl)
tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])
print(tpl)
tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
print(tpl)
tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
print(tpl)
tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
print(tpl)
tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
print(tpl)
tpl = "i am {:s}, age {:d}".format(*["seven", 18])
print(tpl)
tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
print(tpl)
tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
print(tpl)
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)
tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print(tpl)
tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

print(tpl)