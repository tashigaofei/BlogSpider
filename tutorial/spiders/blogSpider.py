__author__ = 'tashigaofei'
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import BlogItem
from scrapy.http import request
from scrapy.contrib.linkextractors.sgml import  SgmlLinkExtractor
from scrapy.contrib.spiders import  Rule, CrawlSpider

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class BlogSpider(CrawlSpider):
    name = 'BlogSpider'
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://news.cnblogs.com/n/197811/"
    ]

    rules = (
        Rule(
            SgmlLinkExtractor(allow=('http://news.cnblogs.com/n/\d+/'),
                              # restrict_xpaths =('//div[@class="prevnext_block"]/a[2]/@href',)
            ),
            callback='parseBlog'),
    )

    def parseBlog(self, response):
        hxs = Selector(response)
        site = hxs.xpath('//div[@id="news_content"]').extract();
        title = hxs.xpath('//div[@id="news_title"]/a/text()').extract();
        item = BlogItem();
        item['title'] = title[0];
        # item['content'] = site[0];
        return item
