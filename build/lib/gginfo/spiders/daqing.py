# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class DaqingSpider(scrapy.Spider):
    name = 'daqing'
    # allowed_domains = ['http://www.dqsbwg.com/view.asp?id=']
    # start_urls = ['http://http://www.dqsbwg.com/view.asp?id=/']

    def start_requests(self):
        start_page = 50
        end_page = 110
        base_url = "http://www.dqsbwg.com/view.asp?id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 37
        name = response.css('body > table:nth-child(3) > tr > td > table > tr > td:nth-child(2) > table > tr:nth-child(2) > td > div > table > tr > td > table > tr > td > table:nth-child(1) > tr:nth-child(2) > td > font > b::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > table:nth-child(3) > tr > td > table > tr > td:nth-child(2) > table > tr:nth-child(2) > td > div > table > tr > td > table > tr > td > table:nth-child(1) > tr:nth-child(3) > td > div > p > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "https://www.wmhg.com.cn"
        url = base_url + str(pic[0]).strip()
        Items['pic'] = url
        # text = response.css('body > div.x-container > div > div.section1 > div > div.slick-cont > div *::text').extract()
        # if (len(text) == 0):
        Items['text'] = ""
        # else:
        #     s = ""
        #     for item in text:
        #         s += str(str(item).strip()).replace('\xa0', '')
        #     Items['text'] = s
        # if Items['text'] == "":
        #     return
        yield Items
