# -*- coding: utf-8 -*-
"""
这个项目用于爬去汽车之家的新车数据
作者：Jzorrof
"""

import scrapy
from tutorial.items import QicheItem

class QicheSpider(scrapy.spider.Spider):
    def parse(self,response):
        pass