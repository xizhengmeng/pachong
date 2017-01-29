# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PicItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
   image_urls = Field()
   images = Field()
   #这里必须用image_urls不能用image_url