# -*- coding: utf-8 -*-
import scrapy
import json


class EluthuUrlsSpiderSpider(scrapy.Spider):
    name = 'eluthu_urls_spider'
    allowed_domains = ['eluthu.com']
    start_urls = ['https://eluthu.com/kavithai-type/பாட்டி_சொன்ன_கதைகள்_%s.html' % page for page in range(1, 37)]

    def parse(self, response):
        kavithi_url_list = []
        kavithai_url = response.css("div.new_kavithai_list_right div.new_kavithai_title a::attr(href)").extract()
        item = [kavithai_url]

        with open('grandmaStoryUrl1.txt', 'a') as f:
            f.write('{0}\n'.format(item[0]))




