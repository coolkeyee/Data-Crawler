# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class AhmSpider(scrapy.Spider):
    name = 'ahm'
    # allowed_domains = ['https://www.ahm.cn/Collection/Details/qtq?nid=']
    # start_urls = ['http://https://www.ahm.cn/Collection/Details/qtq?nid=/']

    def start_requests(self):
        start_page = 300
        end_page = 500
        base_url = "https://www.ahm.cn/Collection/Details/qtq?nid="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 56
        name = response.css('body > div.innercont > div > div.col-detail > div.detail.clearfix > div.cont.fl > h3::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > div.innercont > div > div.col-detail > div.detail.clearfix > div.imgstyle.imgfull.fl > a::attr(href)').extract()
        if (len(pic) == 0):
            return
        base_url = ""
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[-1]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('body > div.innercont > div > div.col-detail > div.detail.clearfix > div.cont.fl > div.synopsis > div.intro > p::text').extract()
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