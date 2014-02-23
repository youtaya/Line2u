# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class OxfordItem(Item):
    # define the fields for your item here like:
    # name = Field()
    link = Field()
    word = Field()

class DoubanItem(Item):
    # define the fields for your item here like:
    nickName = Field()
    link = Field()
    titleName = Field()
    desc = Field()
    photo = Field()
