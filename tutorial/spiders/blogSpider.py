__author__ = 'tashigaofei'
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import BlogItem
from scrapy.http import request ,response
from scrapy.contrib.linkextractors.sgml import  SgmlLinkExtractor
from scrapy.contrib.spiders import  Rule, CrawlSpider

class BlogSpider(CrawlSpider):
    name = 'BlogSpider'
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://news.cnblogs.com/"
    ]

    rules = (
        Rule(
            SgmlLinkExtractor(allow=('http://news.cnblogs.com/n/\d+/'),
                              restrict_xpaths =('//div[@id="news_list"]',)
            ),
            callback='parseBlog',
            follow=False ),
     # Rule(
     #        SgmlLinkExtractor(allow=('http://news.cnblogs.com/n/page/\d{,1}/'),
     #                          restrict_xpaths =('//div[@id="pages"]',)
     #        ),
     #        callback='parseBlog',
     #        follow=True),
    )
    def parseBlog(self, response):
        hxs = Selector(response)
        self.log(response.url)

        # site = hxs.xpath('//div[@id="news_content"]').extract();
        title = hxs.xpath('//div[@id="news_title"]/a/text()').extract();
        if title.__len__() > 0:
            item = BlogItem();
            item['title'] = title[0];
            # item['content'] = site[0];
            return item
