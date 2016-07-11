#! /usr/bin/python
# -*- coding: UTF-8 -*-
'''
使用thread模块创建线程
'''
import thread,time
lk=thread.allocate_lock()
def t1(delay):
	while True:
		lk.acquire()
		print ("[%s] delay %d" % (time.ctime(),delay))
		time.sleep(delay)
		lk.release()
		time.sleep(1)
for i in range(2,10):
	thread.start_new_thread(t1,(i,))
while  True:
	time.sleep(1)