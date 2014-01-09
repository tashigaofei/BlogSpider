# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  json
import  os

class BlogPipeline(object):

    def __init__(self):
        self.file = open(os.path.dirname(os.path.realpath(__file__)) +'/data', 'wb');

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n";
        self.file.write(line);

        return item
