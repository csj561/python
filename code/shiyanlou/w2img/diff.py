#! /usr/bin/python
# -*- coding: UTF-8 -*-

ori = open("w.txt").readlines()#3329个汉字
wk = open("w2.txt").readlines()#3327
for i in range(len(ori)):
	ori[i] = ori[i].strip()
for i in range(len(wk)):
	wk[i] = wk[i].strip()
ori.sort()
wk.sort()
open("w_.txt","w").write("\n".join(ori))
open("w2_.txt","w").write("\n".join(wk))