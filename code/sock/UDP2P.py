#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket,struct,time,thread
def puch_hole(topic,udp_svr):
	'''输入参数topic为第一组洞的唯一标识，upd_svr为UDP服务器的地址(ip,port)
	返回打洞的套接字和对端地址
	'''
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
	sock.sendto(topic,udp_svr)
	buff,addr=sock.recvfrom(1024)
	ip,port=struct.unpack("!4sH",buff)
	ip=socket.inet_ntoa(ip)
	print ((ip,port))
	sock.sendto("ping",(ip,port))
	buff,addr=sock.recvfrom(1024)
	if 'ping' == buff:
		sock.sendto("pong",(ip,port))
	print("handshack[%s]"%buff)
	return sock,(ip,port)

def p2p_svr(addr):
	'''
	UPD服务器，addr为服务器绑定的IP和端口
	'''
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
	sock.bind(addr)
	pairs={}
	while True:
		buff,addr=sock.recvfrom(1024)
		print(buff,addr)
		if buff not in pairs: pairs[buff]=[]
		pair=pairs[buff]
		pair.append(addr)
		if 2 == len(pair):
			print('establish pair[%s]'%buff,pair)
			sock.sendto(socket.inet_aton(pair[0][0])+
				struct.pack("!H",pair[0][1]),pair[1])#网络端字节序列，无符号IP+PORT
			sock.sendto(socket.inet_aton(pair[1][0])+struct.pack("!H",pair[1][1]),pair[0])
			del pairs[buff]
			pass