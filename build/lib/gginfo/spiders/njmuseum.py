# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class NjmuseumSpider(scrapy.Spider):
    name = 'njmuseum'
    # allowed_domains = ['http://www.njmuseumadmin.com/Antique/show/id/']
    # start_urls = ['http://http://www.njmuseumadmin.com/Antique/show/id//']

    def start_requests(self):
        start_page = 50
        end_page = 150
        base_url = "http://www.njmuseumadmin.com/Antique/show/id/"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + ".html"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 49
        name = response.css('#parametertitle::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#ban_pic1 > ul > li:nth-child(1) > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.njmuseumadmin.com"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(2, len(str(pic[-1]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#DB_gallery > div.basicrightcon > div.gundongtiao > p::text').extract()
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
