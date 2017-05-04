#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/2017 12:26 PM
# @Author  : JZK
# @File    : ShoppingCar.py

asset_all = 0
goods_price = 0

car_dict = {}

goods = [
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':10},
    {'name':'显示器','price':1000},
    {'name':'汽车','price':19990},
]

you_Asset = int(input('输入资产：'))

for key, item in enumerate(goods,1):
    print("编号", key, ':' + item['name'], item['price'])

while True:

    good_id = input("请输入商品编号或输入-1结束购买：")

    good_id = int(good_id)
    if good_id == -1:
        break
    elif(good_id >= 1 and good_id <= 4):
        good_name = goods[good_id - 1]['name']
        good_price = goods[good_id -1]['price']
        if(good_name in car_dict):
            #car_dict[good_name] = {'price':good_price,'count':1}
            car_dict[good_name]['count'] += 1
        else:
            car_dict[good_name] = {'price':good_price,'count':1}
    else:
        print('无此商品')
        continue
    temp_price = 0
    for good in car_dict.keys():
        print(good,"单价：", car_dict[good]['price'],'数量：',car_dict[good]['count'])
        temp_price = temp_price + car_dict[good]['price'] * car_dict[good]['count']
    print('商品总价：',temp_price)
    goods_price = temp_price

if(goods_price > you_Asset):
    print('购买失败，金额不足')
else:
    print('购买成功')