# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ScrapyTestPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('test.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists test(地點 varchar(20), 天氣 varchar(20), 溫度 varchar(20), 月平均溫度最低 float, 月平均溫度最高 float, 月平均雨量毫米 float, 月平均雨量毫米日數 float)')
        #pass
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        #pass
    def process_item(self, item, spider):
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into test values({})'
        self.cur.execute(sql.format(placeholders), (item['地點'],item['天氣'],item['溫度'],float(item['月平均溫度最低']),float(item['月平均溫度最高']),float(item['月平均雨量毫米']),float(item['月平均雨量毫米日數'])))
        return item