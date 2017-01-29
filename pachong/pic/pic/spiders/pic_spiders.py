# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from pic.items import PicItem
from scrapy.utils.response import get_base_url

class picSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["jandan.net/ooxx"]

    s_urls = []

    for i in range(2400):
        number = 'page-%i' % i
        string = 'http://jandan.net/ooxx/%s#comments/' % number
        s_urls.append(string)

    start_urls = s_urls

    #这里的关键是把urls存入到item的urls这个字段
    def parse(self, response):
        selector = Selector(response)
        item = PicItem()
        urls = selector.xpath('.//img/@src').extract()
        # item['image_urls'] = urls
        
        images = []

        for url in urls:
            # print 'http:' + url
            urlString = url.encode("utf-8")
            url = 'http:' + urlString
            images.append(url)
            # print item
            # yield item
        
        item['image_urls'] = images 
        yield item

        # yield item
        # for image in images:
        #     print image.extract()
        #     item['image'] = image.extract()
        #     yield item
