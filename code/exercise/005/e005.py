#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
import os
from PIL import Image
if not os.path.exists("out"):
	os.mkdir("out")
for i in os.listdir("./imgs"):
	im = Image.open("./imgs/" + i)

	# resize只能按照比例调整图片文件的大小，返回值是一个新的文件对象，即原对象的一个复本
	im = im.resize( (im.size[0]/3,im.size[1]/3), Image.ANTIALIAS )
	im.save("out/"+i)

#box = (int(left), int(top),int(right),int(bottom))

if not os.path.exists("out2"):
	os.mkdir("out2")
for i in os.listdir("./imgs"):
	im = Image.open("./imgs/" + i)
	'''区域由一个4元组定义，表示为坐标是 (left, upper, right, lower)。 Python Imaging Library 使用左上角为 (0, 0)的坐标系统。'''
	box =(0, 0, im.size[0]*2//3, im.size[1]*2//3)
	im = im.crop(box)
	im.save("out2/"+i)

