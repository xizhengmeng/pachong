# -*- coding: utf-8 -*-

# Scrapy settings for demo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'demo'

SPIDER_MODULES = ['demo.spiders']
NEWSPIDER_MODULE = 'demo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo (+http://www.yourdomain.com)'
# ITEM_PIPELINES = ['novelspider.pipelines.NovelspiderPipeline']

ITEM_PIPELINES = ['demo.pipelines.DemoPipeline']

USER_AGENT = 'MMozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
COOKIES_ENABLED = True

#对mongodb的配置
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'jikexueyuan'
MONGODB_DOCNAME = 'Book'
