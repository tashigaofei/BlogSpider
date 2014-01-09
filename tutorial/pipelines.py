# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  json
import  os
import  codecs

class BlogPipeline(object):

    def __init__(self):
        self.file = codecs.open(os.path.realpath(__file__)+'data', 'w', 'utf-8');

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n";
        self.file.write(line);

        return item
