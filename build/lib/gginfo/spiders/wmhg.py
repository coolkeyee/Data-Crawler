# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class WmhgSpider(scrapy.Spider):
    name = 'wmhg'
    # allowed_domains = ['https://www.wmhg.com.cn/collection/detail/']
    # start_urls = ['http://https://www.wmhg.com.cn/collection/detail//']

    def start_requests(self):
        start_page = 0
        end_page = 500
        base_url = "https://www.wmhg.com.cn/collection/detail/"
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
        name = response.css('body > div.x-container > div > div.t_bannar.r > div > div::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('div.img> img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "https://www.wmhg.com.cn"
        url = base_url + str(pic[0]).strip()
        Items['pic'] = url
        text = response.css('body > div.x-container > div > div.section1 > div > div.slick-cont > div *::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\xa0', '')
            Items['text'] = s
        if Items['text']=="":
            return
        yield Items
