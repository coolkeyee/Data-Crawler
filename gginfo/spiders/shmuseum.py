# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class ShmuseumSpider(scrapy.Spider):
    name = 'shmuseum'
    # allowed_domains = ['https://www.shanghaimuseum.net/museum/frontend/articles/CI0000']
    # start_urls = ['http://https://www.shanghaimuseum.net/museum/frontend/articles/CI0000/']

    def start_requests(self):
        start_page = 4200
        end_page = 4500
        base_url = "https://www.shanghaimuseum.net/museum/frontend/articles/CI0000"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + ".html"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 32
        name = response.css('#collection-detail > div.cp-info-name::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = ""
        pic1=str(pic[-1]).strip()
        pic2=""
        for i in range(2,len(str(pic[-1]).strip())):
            pic2+=pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#collection-detail > div.cp-info-description::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\xa0', '')
            Items['text'] = s
        if Items['text'] == "":
            return
        yield Items
