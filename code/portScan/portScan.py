#! /usr/bin/python
#-*- coding:utf-8 -*-
import nmap
nm=nmap.PortScanner()
print nm.scan("127.0.0.1","12-1000")
print nm.command_line()
print nm.scaninfo()
print nm.all_hosts()
print nm["127.0.0.1"].hostname()
print nm["127.0.0.1"].state()
print nm["127.0.0.1"].all_protocols()
print nm["127.0.0.1"]['tcp'].keys()	