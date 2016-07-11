#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket,struct,time
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(("192.168.137.128",4321))
print("connect OK")
print ( struct.unpack("i", sk.recv(1000))[0])#unpack函数返回元组
sk.send(time.ctime().encode("utf-8"))#string类型必须指定编码

sk.close()