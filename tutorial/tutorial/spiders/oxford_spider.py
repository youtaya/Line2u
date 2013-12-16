from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tutorial.items import OxfordItem
from scrapy.http import Request
from tutorial.utils.select_result import clean_url
from scrapy import log

class DmozSpider(BaseSpider):
    name="oxforddictionaries"
    allowed_domains = ["oxforddictionaries.com"]
    start_urls = [
            "http://www.oxforddictionaries.com/browse/american_english/",
            ]

    def parse(self, response):
        sel = Selector(response)

        for detail_link in sel.xpath('//ul[@class="browseLettersLinks"]/li/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                
                yield Request(url=detail_link, callback=self.parse_detail)

    def parse_detail(self,response):
        sel = Selector(response)
        log.msg("jinxp paras :%s" %response.url,level=log.DEBUG)
        items = []
        sites = sel.xpath('//ul[@class="browseResultList"]/li')
        for site in sites:   
            words = site.xpath('a/span[@class="alpha_title alpha_hw"]/text()').extract()
            log.msg("jinxp words :%s" %words,level=log.DEBUG)
            for word in words:
                item = OxfordItem()
                item['word'] = word
                items.append(item)
            
        return items
