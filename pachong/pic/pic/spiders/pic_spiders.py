# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from pic.items import PicItem
from scrapy.utils.response import get_base_url

class picSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["jandan.net/ooxx"]

    s_urls = []

    for i in range(1000):
        number = 'page-%i' % i
        string = 'http://jandan.net/ooxx/%s#comments/' % number
        s_urls.append(string)

    start_urls = s_urls

    #这里的关键是把urls存入到item的urls这个字段
    #增加一些图片的选择逻辑
    def parse(self, response):
        selector = Selector(response)
        
        # urls = selector.xpath('.//img/@src').extract()
        sels = selector.xpath('//li')
        # item['image_urls'] = urls
        item = PicItem()
        images = []

        for sel in sels:
            url = sel.xpath('./div[1]/div/div[2]/p/img/@src').extract()
            vote = sel.xpath('./div[1]/div/div[2]/div/span[2]/text()').extract()
            if len(vote) > 0:
               print len(vote)   
               voteN = int(vote[0])
               print voteN
               if voteN > 300:
                  print url
                  urlString = url[0].encode("utf-8")
                  urlS = 'http:' + urlString
                  images.append(urlS)

            # item = PicItem()

        # for url in urls:
        #     print url
            # urlString = url.encode("utf-8")
            # url = 'http:' + urlString
            # images.append(url)
        
        item['image_urls'] = images 
        yield item

        # yield item
        # for image in images:
        #     print image.extract()
        #     item['image'] = image.extract()
        #     yield item
