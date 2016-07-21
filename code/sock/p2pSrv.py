#! /usr/bin/python
# -*- coding: UTF-8 -*-
'''
UDP 打洞服务器
'''
import UDP2P

if __name__ == '__main__':
	UDP2P.p2p_svr(('0.0.0.0',18888))
