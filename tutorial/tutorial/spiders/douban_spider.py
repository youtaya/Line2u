from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tutorial.items import DoubanItem
from scrapy.http import Request
from tutorial.utils.select_result import clean_url
from scrapy import log

class DoubanSpider(BaseSpider):
    name="douban"
    allowed_domains = ["douban.com"]
    start_urls = [
            "http://www.douban.com/group/haixiuzu/?ref=sidebar",
            ]

    def parse(self, response):
        sel = Selector(response)

        for detail_link in sel.xpath('//div[@class="group-topics-more"]/a/@herf').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)

                yield Request(url=detail_link, callback=self.parse_detail)

    def parse_detail(self,response):
        sel = Selector(response)
        items = []
        sites = sel.xpath('//ul[@class="browseResultList"]/li')
        for site in sites:
            photos = site.xpath('a/span[@class="alpha_title alpha_hw"]/text()').extract()
            log.msg("jinxp words :%s" %photos,level=log.DEBUG)
            for photo in photos:
                item = DoubanItem()
                item['photo'] = photo
                items.append(item)

        return items
