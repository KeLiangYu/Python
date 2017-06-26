# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    地點 = scrapy.Field()
    天氣 = scrapy.Field()
    溫度 = scrapy.Field()
    月平均溫度最低 = scrapy.Field()
    月平均溫度最高 = scrapy.Field()
    月平均雨量毫米 = scrapy.Field()
    月平均雨量毫米日數 = scrapy.Field()
    #pass
