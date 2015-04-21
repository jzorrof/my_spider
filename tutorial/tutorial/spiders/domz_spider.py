# -*- coding: utf-8 -*-

import scrapy
import sys
from tutorial.items import DmozItem

reload(sys)
sys.setdefaultencoding('utf-8')

class DmozSpider(scrapy.spider.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.autohome.com.cn/newbrand/"
    ]

    def parse(slef, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            #item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['img'] = sel.xpath('a/img/@src').extract()
            item['desc'] = sel.xpath('a/span/text()').extract()
            # desc = sel.xpath('a/span/text()').extract()
            # desc2 =[]
            # for i in desc:
            #     print i
            #     desc2.append(i.encode('utf-8'))
            # item['desc'] = desc2
            yield item
            #print item