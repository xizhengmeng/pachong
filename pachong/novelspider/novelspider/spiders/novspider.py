#codin=utf-8

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from novelspider.items import NovelspiderItem
from scrapy.http.request import Request

class novSpider(CrawlSpider):
    name = "novspider"
    allowed_domains = ["daomubiji.com"]
    # start_urls = ["http://blog.scrapy.org/"]

    def start_requests(self):
        yield Request("http://www.daomubiji.com/",
                      headers={'User-Agent': "MMozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"})

    # redis_key = 'nvospider:start_urls'
    # start_urls = ['http://www.daomubiji.com/']
    # allowed_domains = ["stackoverflow.com"]
    # start_urls = ['http://stackoverflow.com/questions/27686146/scrapy-request-callbacks-not-firing']
    def parse(self, response):
        print (u'hhaha')
        selector = Selector(response)
        table = selector.xpath('//table')
        for each in table:
            bookName = each.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
            content = each.xpath('tr/td/a/text()').extract()
            url = each.xpath('tr/td/a/@href').extract()
            for i in range(len(url)):
                item = NovelspiderItem()
                item['bookName'] = bookName
                item['chapterURL'] = url[i]
                try:
                    item['bookTitle'] = content[i].split(' ')[0]
                    item['chapterNum'] = content[i].split(' ')[1]
                except Exception,e:
                    content

                try:
                    item['chapterName'] = content[i].split(' ')[2]
                except Exception,e:
                    item['chapterName'] = content[i].split(' ')[1][-3:]
                yield item