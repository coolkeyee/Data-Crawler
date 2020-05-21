# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class RjjngSpider(scrapy.Spider):
    name = 'rjjng'
    # allowed_domains = ['http://www.rjjng.com.cn/treasure/yjww.html']
    # start_urls = ['http://http://www.rjjng.com.cn/treasure/yjww.html/']

    def start_requests(self):
        base_url = "http://www.rjjng.com.cn/treasure/yjww.html"
        count = 0
        url = base_url
        count += 1
        yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        detailurl = []
        detailurl = response.css('#view > li > a::attr(href)').extract()
        for baseurl in detailurl:
            url = baseurl
            yield scrapy.Request(url=url, callback=self.detailparse, meta={'id': response.meta['id']})

    def detailparse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 65
        name = response.css('#content_10 > h1::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        # pic = response.css('body > div.innercont > div > div > div.maindetail > div.cont > p:nth-child(1) > strong > img::attr(src)').extract()
        pic = response.css('#content_10 > p:nth-child(3) > a > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = ""
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#content_10 > p:nth-child(4)::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\u3000', '')
            Items['text'] = s.replace('\xa0', '')
        yield Items
