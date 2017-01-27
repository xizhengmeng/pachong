# -*- coding: utf-8 -*-

# Scrapy settings for novelspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
#http://www.daomubiji.com
BOT_NAME = 'novelspider'

SPIDER_MODULES = ['novelspider.spiders']
NEWSPIDER_MODULE = 'novelspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'novelspider (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['novelspider.pipelines.NovelspiderPipeline']

USER_AGENT = ''
COOKIES_ENABLED = True

#对mongodb的配置
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'jikexueyuan'
MONGODB_DOCNAME = 'Book'
