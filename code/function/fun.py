#! /usr/bin/python
# -*- coding: UTF-8 -*-

def fun1(var1,var2):
    "求和函数"
    return var1+var2

print fun1(3,4)

def fun2(var1="default string"):
    "默认参数"
    print var1
fun2()
fun2 ("a ha")

def fun3(name,age):
    "参数顺序可变"
    print "name: ",name
    print "age: ",age
fun3(age=27,name="xyd")

sum = lambda var1,var2:var1+var2
print "sum: ",sum(3,8)