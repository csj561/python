#! /usr/bin/python
# -*- coding: UTF-8 -*-
import os,curses.ascii,string
str="""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
out=""
for c in str:
	if curses.ascii.isalpha(c):
		c= chr(ord(c)+2)
		if not curses.ascii.isalpha(c):
			c= chr(ord(c)-26)
	out+=c

print (out)

def mark():
	"打印分割符"
	print ("---------------------------------------------------")
mark()
def trans_fun(text):
	"函数实现上述功能"
	ret = string.maketrans(string.ascii_lowercase,#仅产生转换table，最后使用translate转换
		string.lowercase[2:]+string.lowercase[:2])
	return string.translate(text,ret)
print (trans_fun(str))
mark()
def get_letters(text):
	"过滤出字母"
	ret = filter(lambda x: x in string.letters,text)
	return ret
file_str = open("mess.txt").read()
print (get_letters(file_str))
mark()
#统计文件中每个字符出现的次数
s = "".join([line.rstrip() for line in open("mess.txt")])
d={}
for c in s:
	d[c]=d.get(c,0)+1
arg=len(s)//len(d)
print ( "".join([c for c in d.keys() if d.get(c) < arg])  )

