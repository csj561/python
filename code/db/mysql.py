#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

#连接数据库
db=MySQLdb.connect("192.168.137.128","root","xyd","myExample")

#获取数据库操作游标
cursor=db.cursor()
#执行SQL语句
cursor.execute("show tables")
tns=[]

#获取所有的执行结果，注：fetchone可以只获取一行
data=cursor.fetchall()
for t in data:
    tn,=t
    tns.append(tn)
print "tables: ",tns
