#! /usr/bin/python
# -*- coding: UTF-8 -*-
import mod1
import sys
mod1.p_hello("xyd")
print sys.path
def split():
    "打印分割符"
    print "-----------------------------------------------"
split()
print dir(mod1)
split()
print globals()
split()
print locals()