__author__ = 'tashigaofei'


import  json
import  os
from scrapy.item import Item, Field
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy import log
from scrapy.exceptions import  DropItem
from scrapy.http.request import Request
from scrapy.utils.project import get_project_settings


class DongwuItem(Item):
    jsonObj = Field();
    path = Field();

class DongwuPipeline(object):

    def process_item(self, item, spider):
        self.file = open(os.path.dirname(os.path.realpath(__file__)) +'/data', 'ab');
        dict = item['jsonObj'];
        if item['path']:
            dict['path'] = item['path'];
        line = json.dumps(dict, ensure_ascii=False) + "\n";
        # line = repr(dict(item)).decode("unicode-escape") + '\n';
        self.file.write(line);
        self.file.close();
        return item


class DongwuFilePipeline(FilesPipeline):

    count = 0;
    storePath = get_project_settings().get(name = 'FILES_STORE')+'/';

    def __init__(self, store_uri, download_func=None):
        super(DongwuFilePipeline, self).__init__(store_uri = store_uri, download_func = download_func);

    def get_media_requests(self, item, info):
        log.msg(format ='start downloading media %(url)s', url= item['jsonObj']['audioURL']);
        yield Request(url =item['jsonObj']['audioURL'], meta={'title' : item['jsonObj']['title']});

    def item_completed(self, results, item, info):
        media_paths = [x['path'] for ok, x in results if ok]
        if media_paths:
            item['path'] = media_paths[0];
        return item;

    def file_path(self, request, response=None, info=None):
        title = request.meta['title'];
        path = title+'_'+os.path.split(request.url)[-1];
        return path;