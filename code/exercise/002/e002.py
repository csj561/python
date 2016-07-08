#!/usr/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
import e001
'''
**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

db =MySQLdb.connect("192.168.137.128","root","xyd","myExample")
data =  [ "(\'"+x+"\')" for x in e001.gen200()]

sql_cmd = 'insert into code_200 values ' + str(data).replace("\"","").replace("]","")[1:]
cursor = db.cursor()
cursor.execute(sql_cmd)
db.commit()
print sql_cmd
