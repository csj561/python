#! /usr/bin/python
#-*- coding:utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WeatherSpider(scrapy.Spider):
	name = 'myweather'
	allowed_domians=['sina.com.cn']
	start_urls=['http://weather.sina.com.cn']
	def parse(self,response):
		item = WeatherItem()
		item['city']=response.xpath()