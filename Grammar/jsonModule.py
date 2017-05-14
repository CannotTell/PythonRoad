#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/14/2017 2:23 PM
# @Author  : JZK
# @File    : jsonModule.py

import json

jsonData1 = '{"name1":"rose1","name2":"rose2","name3":"rose3"}'
jsonData2 = '{"a":"100","b":[{"b1":"b_value1","b2":"b_value2"}, {"b1":"b_value1","b2":"b_value2"}],"c": {"c1":"c_value1","c2":"c_value2"}}'
li = '[12,123,232,3123]'

#json.loads将字符串转换成字典，列表
#反序列化
result1 = json.loads(jsonData1)
result2 = json.loads(jsonData2)
result3 = json.loads(li)

print(type(result1),result1)
print(type(result1),result2)
print(type(result1),result3)

#序列化 load和dump一般处理文件
result1 = json.dumps(result1)
result2 = json.dumps(result2)
result3 = json.dumps(result3)

print(type(result1),result1)
print(type(result1),result2)
print(type(result1),result3)