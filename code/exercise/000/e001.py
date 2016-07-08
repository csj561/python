#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
**第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
类似于图中效果
![头像](http://i.imgur.com/sg2dkuY.png?1)
'''

import os
from PIL import Image,ImageFont,ImageDraw

ori_img = 'e001_ori.png'
out_img = 'e001.png'
font_file = 'simkai.ttf'
os.system("cp " + ori_img + " " + out_img)

im = Image.open(out_img)#载入一个图片对象
font = ImageFont.truetype(font_file,46)#载入一个字库对象，并且设置字体大小

draw= ImageDraw.Draw(im)#创建一个绘画对象
font_size=min(im.size)/8
#draw.text((im.size[0]-font_size,0),"2",(255,0,0),font)
draw.text((0,0),"徐".decode("UTF-8"),(255,0,0),font)#将文件绘制到绘画对象上面

im.save("aa.png")#将图片对象另存为xxx
