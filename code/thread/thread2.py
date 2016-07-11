#! /usr/bin/python
# -*- coding: UTF-8 -*-
'''
使用threading模块创建线程

threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
'''
import time,threading
class myThread(threading.Thread):
	def __init__(self,delay,lock):
		threading.Thread.__init__(self)
		self.dly=delay
		self.lk=lock
	def run(self):
		while True:
			self.lk.acquire()
			print ("[%s] delay %d" % (time.ctime(),self.dly))
			time.sleep(self.dly)
			self.lk.release()
			time.sleep(1)
th_ls=[]
lock=threading.Lock()
for i in range(2,10):
	t=myThread(i,lock)
	t.start();
	th_ls.append(t)
for i in th_ls: t.join()