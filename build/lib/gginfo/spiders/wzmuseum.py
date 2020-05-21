# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class WzmuseumSpider(scrapy.Spider):
    name = 'wzmuseum'
    # allowed_domains = ['http://www.wzmuseum.cn/Art/Art_28/Art_28_']
    # start_urls = ['http://http://www.wzmuseum.cn/Art/Art_28/Art_28_/']

    def start_requests(self):
        start_page = 3280
        end_page = 3350
        base_url = "http://www.wzmuseum.cn/Art/Art_28/Art_28_"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)+".aspx"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 55
        name = response.css('body > div > div.row-middle2 > div.newcontainer > div.newstitle-box > div.newstitle::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > div > div.row-middle2 > div.newcontainer > div.newstxt > div:nth-child(1) > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.wzmuseum.cn"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('body > div > div.row-middle2 > div.newcontainer > div.newstxt > div:nth-child(4) *::text').extract()
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
