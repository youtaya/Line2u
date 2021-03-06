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
            "http://www.douban.com/group/haixiuzu/discussion?start=0",
            ]

    def parse(self, response):
        response_selector = Selector(response)
        next_link = response_selector.select(u'//span[@class="next"]/a/@href').extract()[0]
        log.msg("jinxp next link is %s" % next_link, level=log.DEBUG)
        if next_link:
            next_link = clean_url(response.url,next_link,response.encoding)
            yield Request(url=next_link, callback=self.parse)

        for detail_link in response_selector.select(u'//table[@class="olt"]/tr[@class=""]/td[@class="title"]/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                yield Request(url=detail_link, callback=self.parse_detail)                

    def parse_detail(self,response):
        sel = Selector(response)
        item = DoubanItem()
 
        log.msg("jinxp parse detail url is %s" % response.url, level=log.DEBUG)
        titleBar = sel.xpath('//div[@id="content"]/h1/text()').extract()
        contentAuthor = sel.xpath('//div[@class="topic-doc"]/h3/span[@class="from"]/a/text()').extract()
        photos = sel.xpath('//div[@class="topic-content"]/div[@class="topic-figure cc"]/img/@src').extract()
        download = []
        for photo in photos:           
            download_item = {}
            download_item['url'] = photo
            download.append(download_item)
        item['titleName'] = titleBar[0]
        item['nickName'] = contentAuthor[0]
        item['photo'] = download

        return item
