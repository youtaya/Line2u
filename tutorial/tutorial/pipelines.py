# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log

class TutorialPipeline(object):

    def __init__(self):
        self.file = open('dump.txt' , 'w')

    def process_item(self, item, spider):
        log.msg("jinxp item is %s, spider is %s" % (item, spider), level=log.DEBUG)

        if item['word']:
            self.file.write(str(item['word'].encode("utf-8").strip(" -").replace(",", "").lower())+ '\n')
        return item
