__author__ = 'tashigaofei'
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tutorial.items import DmozItem


class DmozSpider(BaseSpider):
    name = 'DmozSpider'
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://news.cnblogs.com/n/197616/"
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     open(filename, 'wb').write(response.body)


    # def parse(self, response):
    # hxs = HtmlXPathSelector(response)
    # sites = hxs.select('//fieldset/ul/li')
    # #sites = hxs.select('//ul/li')
    # for site in sites:
    # title = site.select('a/text()').extract()
    # link = site.select('a/@href').extract()
    # desc = site.select('text()').extract()
    # #print title, link, desc
    # print title, link
    # #print title


    def parse(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//div[@id="news_content"]')
        # open(filename, 'wb').write(response.body)
        items = []
        for site in sites:
            item = DmozItem()
            item['content'] = site.extract()
            items.append(item)
        return items
