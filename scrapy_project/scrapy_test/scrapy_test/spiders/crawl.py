# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from scrapy_test.items import ScrapyTestItem

class TestCrawler(scrapy.Spider):
    name = 'test'
    start_urls = ['http://www.cwb.gov.tw/V7/forecast/world/world_aa.htm']
    def parse(self, response):
        
        domain = 'http://www.cwb.gov.tw'
        res = BeautifulSoup(response.body,'lxml')
        for i in range(1,5):
            for news in res.select('.Forecast5' + str(i)):
                yield scrapy.Request(domain + news['href'],self.parse_detail)
                #yield scrapy.Request(domain + news.select('a')[0]['href'],self.parse_detail)
    def parse_detail(self, response):
        res = BeautifulSoup(response.body,'lxml')
        data = []
        testitem = ScrapyTestItem()
        rows = res.select('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text for ele in cols]
            data.append(cols)
        for news in data[3:len(data)-1]:
            testitem['地點'] = news[0]
            testitem['天氣'] = news[1]
            testitem['溫度'] = news[2]
            testitem['月平均溫度最低'] = news[3]
            testitem['月平均溫度最高'] = news[4]
            testitem['月平均雨量毫米'] = news[5]
            testitem['月平均雨量毫米日數'] = news[6]
            yield testitem