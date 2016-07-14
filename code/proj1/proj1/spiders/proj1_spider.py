#! /usr/bin/python
#-*- coding:utf-8 -*-

import scrapy
from proj1.items import Proj1Item

class Proj1Spider(scrapy.Spider):
	name='proj1'
	allowed_domains=['www.weather.com.cn']
	start_urls=['http://www.weather.com.cn/weather/101270101.shtml']
	cnt = 0
	def parse(self,response):
		item = Proj1Item()
		item['city']='chengdu'
		item['date']=response.css('#7d li > h1::text').extract()
		item['day']=response.css('#7d li>p> span::text').extract()
		item['light']=response.css('#7d li>p>i::text').re('^\d.*')
		return item
