#! /bin/sh

#功能：	1，将dos格式的python文件转换为unix格式
#	2，但是不改为文件的修改时间
while [ 1 -eq 1 ]
do

files=`find . -name *.py`

for i in $files
do
	is_dos=`file $i |grep CRLF`;
	if [ -n "$is_dos" ]
	then
		#获取文件的修改时间，保存到i_time
		i_time=`stat $i |grep Modify|awk  '{print $2 $3}'|sed 's/\..*$//g'|sed 's/\-//g'|awk -F ':' '{print $1 $2 "." $3}'`
		dos2unix $i > dos2unix.log 2>&1
		touch -t $i_time $i
	fi
done
sleep 3;
done
