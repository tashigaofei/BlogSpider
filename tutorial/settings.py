# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os
BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
ITEM_PIPELINES = {'tutorial.pipelines.BlogPipeline': 0 }
# LOG_STDOUT = True
# LOG_FILE = os.path.dirname(os.path.realpath(__file__))+'/logfile'
# LOG_ENABLE = True

#FEED_URI = os.path.dirname(os.path.realpath(__file__)) + '/data';
#FEED_FORMAT = 'jsonlines'
# DOWNLOAD_DELAY = 0.020
# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
# LOG_LEVEL =  'DEBUG'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 0,
}