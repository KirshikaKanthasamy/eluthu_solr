# -*- coding: utf-8 -*-
import scrapy
import json


class EluthuSpiderSpider(scrapy.Spider):
    name = 'eluthu_spider'
    allowed_domains = ['eluthu.com']

    with open('./cleaned_urls/jokeUrlCleaned.txt') as json_file:
        dataUrls = json.load(json_file)
    start_urls = dataUrls

    def parse(self, response):

        title = response.css('h1.post_title::text').extract_first()
        sub_type = response.css('div.eluthu_tags li a::text').extract_first()
        author = response.css('span.author_blue::text').extract_first()
        content = response.css('p.post_desc::text').extract_first()
        written_date = response.css('span.author_red::text').extract_first()
        uploaded_by = response.css('span.author_red a::text').extract_first()
        views = response.css('span.author_views span.author_red::text').extract_first()

        eluthu_items = [title, sub_type, author, content, written_date, uploaded_by, views]


        eluthu_items_list = {
            "தலைப்பு": eluthu_items[0],
            "வகை": "நகைச்சுவை",
            "உபவகை": eluthu_items[1],
            "எழுதியவர்": eluthu_items[2],
            "உள்ளடக்கம்": eluthu_items[3],
            "எழுதிய_திகதி": eluthu_items[4],
            "பதிவேற்றியவர்": eluthu_items[5],
            "பார்வைகள்": eluthu_items[6]
        }

        # with open('./data/gs.txt', 'a') as f:
        #     f.write('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}\n'.format(eluthu_items[0], 'பாட்டி_சொன்ன_கதைகள்', eluthu_items[1], eluthu_items[2], eluthu_items[3], eluthu_items[4], eluthu_items[5], eluthu_items[6]))
        yield eluthu_items_list
