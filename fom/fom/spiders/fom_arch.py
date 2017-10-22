# -*- coding: utf-8 -*-
import scrapy


class FomArchSpider(scrapy.Spider):
    name = 'fom_arch'
    allowed_domains = ['www.cs.nyu.edu/pipermail/fom/']
    start_urls = ['http://www.cs.nyu.edu/pipermail/fom//']

    def parse(self, response):
        pass
