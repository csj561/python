#! /usr/bin/python
# -*- coding: UTF-8 -*-

#if判断用法
name = "xyd"
if name == 'hk' :
    print "name is hk" 
elif ("xyd" == name):
    print "name is " + name
else:
    print "Unknown"

#while用法
print "print even"
a=10
while a>0 :
    a-=1
    if a%2:
        continue
    print a

while 1:
    a+=1;
    if a>10:
        break;
    print a
#while else用法
b=0
while b<=3:
    print b,"小等于3"
    b+=1
else:
    print b,"大于3"
