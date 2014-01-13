__author__ = 'tashigaofei'
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.blogItem import BlogItem
from scrapy.http import Request ,Response
from scrapy.contrib.linkextractors.sgml import  SgmlLinkExtractor
from scrapy.contrib.spiders import  Rule, CrawlSpider
import urlparse

class BlogSpider(CrawlSpider):
    name = 'BlogSpider'
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://news.cnblogs.com/"
    ]

    def parse(self, response):
        hxs = Selector(response)
        self.log(response.url)

        for item in hxs.xpath('//div[@id="news_list"]').re('/n/\d+/'):
            urlString = urlparse.urljoin(response.url, item);
            yield Request(url =urlString, callback = self.blogParse)

        for item in hxs.xpath('//div[@id="pages"]').re('/n/page/\d{,1}/'):
            urlString = urlparse.urljoin(response.url, item);
            yield Request(url =urlString, callback = self.parse)


    def blogParse(self, response):
        hxs = Selector(response)
        # site = hxs.xpath('//div[@id="news_content"]').extract();
        title = hxs.xpath('//div[@id="news_title"]/a/text()').extract();
        if title.__len__() > 0:
            item = BlogItem();
            item['title'] = title[0];
            # item['content'] = site[0];
            return item