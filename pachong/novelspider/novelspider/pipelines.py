# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class NovelspiderPipeline(object):
    def __init__(self):
       host = settings['MONGODB_HOST']
       port = settings['MONGODB_PORT']
       dbName = settings['MONGDB_DBNAME']
       clinet = pymongo.MongoClient(host=host, port=port)
       tdb = clinet[dbName]
       self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        bookInfo = dict(item)#将item转换成字典
        self.post.insert(bookInfo)#将字典插入数据库
        return item
