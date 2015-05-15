# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

from boto.s3.connection import S3Connection
from boto.s3.key import Key


class TutorialPipeline(object):
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.file = codecs.open('qiche.json', 'wb', encoding='utf-8')
        self.bucketname = 'scrapy_data_2'
        self.conn = S3Connection()
        self.getbucket = self.conn.get_bucket(self.bucketname)
        self.k = Key(self.getbucket)

    def process_item(self, item, spider):
        if item['desc']:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(line)
            return item
        else:
            pass
            # raise DropItem("Missing price in %s" % item)

    def spider_closed(self, spider):
        print('closing~~~~~~~~')
        '''
        connection to Amazon S3
        android create bucket for story scrapy_data
        '''
        self.k.key = 'my_scrapy'
        self.k.set_contents_from_filename('qiche.json')
        self.file.close()