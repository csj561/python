#! /usr/bin/python
# -*- coding: UTF-8 -*-

import time

print "now time: ",time.localtime()
'''
结果字段
序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''

'''
相关函数


序号	函数及描述
1	time.altzone
    返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
2	time.asctime([tupletime])
    接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
3	time.clock( )
    用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
4	time.ctime([secs])
    作用相当于asctime(localtime(secs))，未给参数相当于asctime()
5	time.gmtime([secs])
    接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
6	time.localtime([secs])
    接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
7	time.mktime(tupletime)
    接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
8	time.sleep(secs)
    推迟调用线程的运行，secs指秒数。
9	time.strftime(fmt[,tupletime])
    接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
    根据fmt的格式把一个时间字符串解析为时间元组。
11	time.time( )
    返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
12	time.tzset()
    根据环境变量TZ重新初始化时间相关设置。
    Time模块包含了以下2个非常重要的属性：
序号	属性及描述
1	time.timezone
    属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
2	time.tzname
    属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
'''