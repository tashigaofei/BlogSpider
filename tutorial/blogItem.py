# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import  json
import  os
from scrapy.item import Item, Field

class BlogItem(Item):
    title = Field();
    content = Field();

class BlogPipeline(object):

    def __init__(self):
        self.file = open(os.path.dirname(os.path.realpath(__file__)) +'/data', 'wb');

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n";
        # line = repr(dict(item)).decode("unicode-escape") + '\n';
        self.file.write(line);

        return item
