#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket,struct,time,binascii,thread,sys

class ImTester:
        """docstring for ImTester"""
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        def __init__(self, arg):
                self.sock.connect(arg)
        def __del__(self):
                self.sock.close()

        def recv(self):
                """get pack from socket"""
                buf=self.sock.recv(1024,0)
                if len(buf) < 12:
                        if len(buf) <=0:
                                print ("socket disconnect")
                                sys.exit(-1)
                        print ("the receved buf is small")
                        return ""
                mark,slen,crc32,json=struct.unpack("!4sii%ds"%(len(buf)-12),buf)
                if slen+12!=len(buf):
                        print("len missmatch expect len[%d] realy len[%d]"%(slen+12,len(buf)))
                        return ""
                if "json" != mark:
                        print ("Not start with 'josn' ")
                        return ""
                if crc32 != binascii.crc32(json):
                        print ("crc32 missmatch")
                        return ""
                #print("json [%s]",json)
                return json
        def send(self,json2):
                """send to socket"""
                jlen= len(json2)
                icrc32=binascii.crc32(json2)
                fmt="!4sii%ds"%jlen
                self.sock.send(struct.pack(fmt,"json",jlen,icrc32,json2))# 1， icrc32不能强转为int否则会出错，2，pack的结果不能转为utf8,否则出错

def testRecv(sk):
        while True:
                print ("recv [%s]" % sk.recv())
def testSend(sk,_s):
        while True:
                sk.send(_s)
                time.sleep(1200)
s_register='''{
   "msg_id":4,
        "sequence":444,
        "module_name": "py",
        "module_address": "1.1.1.1",
        "module_type":0,
        "user_id":"aaaaaaaa"
}
'''
if __name__ == '__main__':
        im = ImTester(("10.0.5.182",8888))
        thread.start_new_thread(testRecv,(im,))
        thread.start_new_thread(testSend,(im,s_register,))
        while True:
                time.sleep(1)
                
