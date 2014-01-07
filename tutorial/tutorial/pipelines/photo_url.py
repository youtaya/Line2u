#!/usr/bin/python
#-*-coding:utf-8-*-

import os
from scrapy import log
from scrapy.http import Request
from scrapy.contrib.pipeline.images import ImagesPipeline

class DoubanImage(ImagesPipeline):
    """
    this is for download the book covor image and then complete the
    book_covor_image_path field to the picture's path in the file system.
    """
    def __init__(self, photo_uri, download_func=None):
        self.images_store = photo_uri
        super(DoubanImage,self).__init__(photo_uri, download_func=None)

    def get_media_requests(self, item, info):
        if item.get('photo'):
            for url in item['photo']:
                yield Request(url['url'])

    def item_completed(self, results, item, info):
        if self.LOG_FAILED_RESULTS:
            msg = '%s found errors proessing %s' % (self.__class__.__name__, item)
            for ok, value in results:
                if not ok:
                    log.err(value, msg, spider=info.spider)

        image_paths = [x['path'] for ok, x in results if ok]
        image_path = image_paths[0]
        item['desc'] = os.path.join(os.path.abspath(self.images_store),image_path) if image_path else ""

        return item
