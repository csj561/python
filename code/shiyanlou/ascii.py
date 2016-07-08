#! /usr/bin/python
# -*- coding: UTF-8 -*-

#将图个转化为字符
from PIL import Image
import argparse

#这个列表左边的字符灰度值比较大，右边的小
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#灰度值 ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

def get_char(r,b,g,alpha=256):
    "RGB像素映射字符"
    if 0==alpha:
        return " "
    length=len(ascii_char)
    gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]

parser = argparse.ArgumentParser ()
parser.add_argument("file")
parser.add_argument("-o","--output")

parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

args=parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

if __name__ == "__main__":#直接执行的这个脚本
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
