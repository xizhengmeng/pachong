# -*- coding: utf-8 -*-

# Scrapy settings for pic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pic'

SPIDER_MODULES = ['pic.spiders']
NEWSPIDER_MODULE = 'pic.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pic (+http://www.yourdomain.com)'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '/Users/shenghuihan/Desktop/picture'

USER_AGENT = 'MMozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
COOKIES_ENABLED = True