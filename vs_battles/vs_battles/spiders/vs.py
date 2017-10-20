# -*- coding: utf-8 -*-
import scrapy


class VsSpider(scrapy.Spider):
    name = 'vs'
    allowed_domains = ['vsbattles.wikia.com']
    start_urls = ['http://vsbattles.wikia.com/']

    def parse(self, response):
        print("############")
        print(response)
