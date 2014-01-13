__author__ = 'tashigaofei'

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request, Response
import urlparse
import  json
from tutorial.dongwuItem import DongwuItem
from scrapy.item import Item, Field

class DongwuSpider(Spider):
    name = 'DongwuSpider'
    allowed_domains = ["app.21sq.org/"]
    siteURL = "http://app.21sq.org/radio/dongwuLists?catid=631&page=%d"
    pageIndex = 1;
    count = 0;

    def start_requests(self):
        yield self.make_requests_from_url(self.siteURL % self.pageIndex);

    def parse(self, response):
        if response.body:
            self.pageIndex = self.pageIndex + 1;
            yield self.make_requests_from_url(self.siteURL % self.pageIndex);

            jsonObject = json.loads(response.body);
            for obj in jsonObject['audioList']:
                dongwuItem  = DongwuItem();
                dongwuItem['jsonObj'] = obj;
                yield dongwuItem;