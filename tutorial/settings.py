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
# ITEM_PIPELINES = {'tutorial.pipelines.BlogPipeline': 0 }

ITEM_PIPELINES = {'tutorial.dongwuItem.DongwuFilePipeline': 0,
                  'tutorial.dongwuItem.DongwuPipeline': 1
                  }

LOGSTATS_INTERVAL = 5.0
DOWNLOAD_TIMEOUT = 10*60
FILES_STORE = os.path.dirname(os.path.realpath(__file__))+'/DongwuDownloads';

CONCURRENT_ITEMS = 40
CONCURRENT_REQUESTS = 40
CONCURRENT_REQUESTS_PER_DOMAIN = 40

# COOKIES_ENABLED = False;
# LOG_STDOUT = True
# LOG_FILE = os.path.dirname(os.path.realpath(__file__))+'/logfile'
# LOG_ENABLE = True
USER_AGENT = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'

#FEED_URI = os.path.dirname(os.path.realpath(__file__)) + '/data';
#FEED_FORMAT = 'jsonlines'
DOWNLOAD_DELAY = 0.010
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
# LOG_LEVEL =  'DEBUG'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 0,
}