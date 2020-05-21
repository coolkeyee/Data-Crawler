# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class HzmuseumSpider(scrapy.Spider):
    name = 'hzmuseum'
    # allowed_domains = ['http://www.hzmuseum.com/collectioninfo.aspx?nid=']
    # start_urls = ['http://http://www.hzmuseum.com/collectioninfo.aspx?nid=/']

    def start_requests(self):
        start_page = 87
        end_page = 259
        base_url = "http://www.hzmuseum.com/collectioninfo.aspx?nid="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 54
        name = response.css('#form1 > div.ff > div.ffrg.rg > div.ffrg2 > div > div.biaoti::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#form1 > div.ff > div.ffrg.rg > div.ffrg2 > div > p:nth-child(3) > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.hzmuseum.com"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(2, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#form1 > div.ff > div.ffrg.rg > div.ffrg2 > div > p:nth-child(10) > span::text').extract()
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
