# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Proj1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city=scrapy.Field()
    date=scrapy.Field()
    day=scrapy.Field()
    light=scrapy.Field()
    pass
