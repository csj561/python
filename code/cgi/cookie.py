#! /usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
import os
import Cookie

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')#上传来的cookie保存在环境变量中
    c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['name'].value#通过cookie名获取cookie
        print "cookie data: "+data+"<br>"
    except KeyError:
        print "cookie 没有设置或者已过去<br>"