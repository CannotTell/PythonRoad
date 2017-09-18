#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/12/2017 4:15 PM
# @Author  : JZK
# @File    : demo_1.py

import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World')


application = tornado.web.Application([
    (r'/index', MainHandler),
])


if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()