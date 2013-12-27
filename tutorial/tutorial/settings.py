# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
PROJ_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

#ITEM_PIPELINES = ['tutorial.pipelines.TutorialPipeline']
ITEM_PIPELINES = ['tutorial.pipelines.store.DoubanPipeline',
				'tutorial.pipelines.photo_url.DoubanImage']

IMAGES_STORE = os.path.join(PROJ_DIR,'media/photo_image')
