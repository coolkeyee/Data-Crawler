# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class A1991mSpider(scrapy.Spider):
    name = '1991m'
    # allowed_domains = ['http://www.1911museum.com/Collection/Details/zgww?nid=']
    # start_urls = ['http://http://www.1911museum.com/Collection/Details/zgww?nid=/']

    def start_requests(self):
        start_page = 300
        end_page = 401
        base_url = "http://www.1911museum.com/Collection/Details/zgww?nid="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 83
        name = response.css('body > div.innercont > div.allcenter > div.maindetail > div.title::text').extract()
        name = response.css('body > div.innercont > div.allcenter > div.maindetail > div.title::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > div.innercont > div.allcenter > div.maindetail > div.cont > p:nth-child(1) > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = ""
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('body > div.innercont > div.allcenter > div.maindetail > div.cont *::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\u3000', '')
            Items['text']=s
        yield Items
