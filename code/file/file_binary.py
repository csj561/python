#! /usr/bin/python
# -*- coding: UTF-8 -*-

import struct
fn2='file-bin.txt'
fp=open(fn2,"rb")
bytes=fp.read(10)
fp.close()

# unpack 返回的是元组，因此要用以下格式获取其中的元素
i,=struct.unpack("i",bytes)
print "read: ",i

h1,h2=struct.unpack("hh",bytes)
print "short: ",h1,h2

'''
转化时支持的类型

Format	C Type	Python	字节数
x	pad byte	no value	1
c	char	string of length 1	1
b	signed char	integer	1
B	unsigned char	integer	1
?	_Bool	bool	1
h	short	integer	2
H	unsigned short	integer	2
i	int	integer	4
I	unsigned int	integer or long	4
l	long	integer	4
L	unsigned long	long	4
q	long long	long	8
Q	unsigned long long	long	8
f	float	float	4
d	double	float	8
s	char[]	string	1
p	char[]	string	1
P	void *	long
'''

'''
对齐方式
Character	Byte order	Size and alignment
@	native	native            凑够4个字节,默认
=	native	standard        按原字节数
<	little-endian	standard        按原字节数
>	big-endian	standard       按原字节数
!	network (= big-endian)	standard       按原字节数
 

使用方法是放在fmt的第一个位置，就像'@5s6sif'
'''

s=struct.pack("2i",3,5)
print "s len: ",len(s)

s=struct.pack("=hi",3,8)
print "s len: ",len(s)# output 6

s=struct.pack("hi",3,8)
print "s len: ",len(s)# output 8, the same as  @hi