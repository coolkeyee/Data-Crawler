# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class KfsmSpider(scrapy.Spider):
    name = 'kfsm'
    allowed_domains = ['http://www.kfsbwg.com/html/2016/yuqi_0815/']
    start_urls = ['http://http://www.kfsbwg.com/html/2016/yuqi_0815//']

    def start_requests(self):
        start_page = 102
        end_page = 109
        base_url = "http://www.kfsbwg.com/html/2016/yuqi_0815/"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + ".html"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 78
        name = response.css('#list > div.r > div > h4::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = ""
        pic1 = str(pic[2]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[2]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#list > div.r > div > p:nth-child(4) *::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\u3000', '')
            Items['text'] = s.replace('\xa0', '')
        if Items['text'] == "":
            return
        yield Items
