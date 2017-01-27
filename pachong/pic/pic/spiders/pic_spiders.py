


from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from pic.items import PicItem

class picSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = ["http://tieba.baidu.com/p/4392110523"]

    #这里的关键是把urls存入到item的urls这个字段
    def parse(self, response):
        selector = Selector(response)
        item = PicItem()
        urls = selector.xpath('//*[@id="post_content_85113691760"]/img/@src').extract()
        images = selector.xpath('//*[@id="post_content_85113691760"]/img')
        item['image_urls'] = urls

        print urls
        for url in urls:
            print url
            # item['image_url'] = url
            # yield item

        yield item
        # for image in images:
        #     print image.extract()
        #     item['image'] = image.extract()
        #     yield item
