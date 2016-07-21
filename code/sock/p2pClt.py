#! /usr/bin/python
# -*- coding: UTF-8 -*-

'''
UDP 打洞客户端
'''
import socket,struct,time,thread,UDP2P
def th_snd(sock_fd,addr):
	"send buff fps"
	while True:
		sock_fd.sendto(socket.gethostname().encode('utf-8'),addr)
		time.sleep(5)
		pass
def th_rcv(sock_fd):
	'recv buff,and print'
	while True:
		print(sock_fd.recvfrom(1024)[0].decode('utf-8'))
		pass

if __name__ == '__main__':	
	sock,addr=UDP2P.puch_hole("P2P2",("192.168.137.128",18888))
	thread.start_new_thread(th_rcv,(sock,))
	thread.start_new_thread(th_snd,(sock,addr))
	while True:
		time.sleep(10)