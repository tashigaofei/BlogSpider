__author__ = 'tashigaofei'

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from tutorial.spiders.blogSpider import BlogSpider
from tutorial.spiders.dongwuSpider import DongwuSpider
from scrapy.utils.project import get_project_settings
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# spider = BlogSpider(domain='cnblogs.com')
spider = DongwuSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel = 'DEBUG', logstdout=True);
# log.start(logfile = os.path.dirname(os.path.realpath(__file__))+'logfile', loglevel = 'DEBUG');
reactor.run() # the script will block here until the spider_closed signal was sent