#! /usr/bin/python
# -*- coding: UTF-8 -*-
import pygame,sys
from PIL import Image
import os,StringIO
f=open("word.txt")
words = f.readlines()[0].strip()
f.close()
def pasteWord(words):
	"渲染文字的函数"
	wd="/home/xyd/pycode_git/shiyanlou/w2img/word"
	if not os.path.exists(wd):
		os.mkdir(wd)
	#os.chdir(wd)
	font_path="/home/xyd/pycode_git/shiyanlou/w2img/simkai.ttf"
	'''
	必须用root权限来执行

	Try looking at the permission of /dev/dsp and /dev/snd/* . If you don't have read write permission on these files then no sound is possible.
	'''
	pygame.init()
	font = pygame.font.Font(font_path,22)
	text_list = words.split(" ")
	length = len(text_list)

	for i in range(length):
		text = text_list[i].decode("utf-8","ignore")
		imgName = text_list[i]+".png"
		if os.path.isfile(imgName):
			continue
		else:
			paste(text,font,imgName)

def paste(text,font,imgName,area=(5,3)):
	"渲染文字生成图片"
	im = Image.new("RGB",(30,30),(255,255,255))
	rtext = font.render(text,True,(0,0,0),(255,255,255,))
	sio = StringIO.StringIO()
	pygame.image.save(rtext,sio)
	sio.seek(0)
	line=Image.open(sio)
	im.paste(line,area)
	im.save(imgName)

pasteWord(words)
