#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/23/2017 4:39 PM
# @Author  : JZK
# @File    : 金拱门asyncio.py
import asyncio
import random


async def jingongmen(_id, que):
    for i in range(10):
        print('金拱门{}生产汉堡{}{}..'.format(_id, _id, i))
        msg = await que.put('{}{}'.format(_id, i))
        if msg == -1:
            print('金拱门{}结束'.format(_id))
            return
        print('汉堡{}{}完成'.format(_id, i))
        await asyncio.sleep(random.randrange(1, 3))

    print('金拱门{}关闭..'.format(_id))
    await que.put(-1)


async def _me(_id, que):
    while True:
        print('{}号我需要一个汉堡'.format(_id))
        hanbao = await que.get()
        if hanbao == -1:
            print('{}号我结束'.format(_id))
            return
        print('{}号拿到汉堡{}'.format(_id, hanbao))
        que.task_done()
        await asyncio.sleep(random.randrange(1, 3))


if __name__ == '__main__':
    que = asyncio.Queue(50)
    loop = asyncio.get_event_loop()
    # me_list = [_me(i, que) for i in range(3)]
    # jgm_list = [jingongmen(j, que) for j in range(2)]
    # me_list.extend(jgm_list)
    task_list = [jingongmen(1, que), _me(1, que), _me(2, que), jingongmen(2, que)]
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()