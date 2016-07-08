#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import random

#print ("%08X" % random.randrange(1000000,4*10**9))
def gen200():
	"产生200个不重复的激活码"
	ret =[]
	while True:
		num="%08X" % random.randrange(1000000,4*10**9)
		if num not in ret:
			ret.append(num)
		if 200 == len(ret):
			break
	return ret

if __name__ == '__main__':
	print (gen200())
