#! /usr/bin/python
# -*- coding: UTF-8 -*-
import re
import sys

p=re.compile("c")
str='abcabcabc'
l=p.split(str)#返回做分割后的字串列表
print l
s=p.sub("C",str)#返回新串
print s
s2=p.subn("C",str)#元组(新串，次数)

print s2