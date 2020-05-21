# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class AymSpider(scrapy.Spider):
    name = 'aym'
    # allowed_domains = ['http://www.aymuseum.com/nd.jsp?id=766#_jcp=4_2']
    # start_urls = ['http://http://www.aymuseum.com/nd.jsp?id=766#_jcp=4_2/']

    def start_requests(self):
        start_page = 766
        end_page = 770
        base_url = "http://www.aymuseum.com/nd.jsp?id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)+"#_jcp=4_2"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 67
        name = response.css('#module12 > div.formMiddle.formMiddle12 > div.formMiddleCenter.formMiddleCenter12 > div > div > h1::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#module12 > div.formMiddle.formMiddle12 > div.formMiddleCenter.formMiddleCenter12 > div > div > div.richContent.richContent0 > p > span > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http:"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#module12 > div.formMiddle.formMiddle12 > div.formMiddleCenter.formMiddleCenter12 > div > div > div.richContent.richContent0 *::text').extract()
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
