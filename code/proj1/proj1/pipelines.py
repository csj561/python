# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Proj1Pipeline(object):
    def process_item(self, item, spider):
    	with open('wea.txt','w') as fp:
    		city=item['city']
    		days=item['day']
    		lights=item['light']
    		dates=item['date']
    		wea=zip(dates,days,lights)
    		for i in wea:
    			date=i[0].encode('utf-8')
    			day=i[1].encode('utf-8')
    			light=i[2].encode('utf-8')
    			fp.write("{0}\t{1}\t{2}\t{3}\n\n".format(
    				city,date,day,light))
        return item
