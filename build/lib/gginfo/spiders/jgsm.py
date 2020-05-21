# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class JgsmSpider(scrapy.Spider):
    name = 'jgsm'
    # allowed_domains = ['http://www.jgsgmbwg.com/productshow.php?cid=6&id=']
    # start_urls = ['http://http://www.jgsgmbwg.com/productshow.php?cid=6&id=/']

    def start_requests(self):
        start_page = 20
        end_page = 28
        base_url = "http://www.jgsgmbwg.com/productshow.php?cid=6&id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 63
        name = response.css('#top > div.subBody > div.OneOfTwo > div > h1::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#top > div.subBody > div.OneOfTwo > div > div.showimg > a > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.jgsgmbwg.com"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#textarea > span::text').extract()
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
