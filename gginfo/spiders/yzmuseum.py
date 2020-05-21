# -*- coding: utf-8 -*-
import scrapy
import scrapy
import bs4
import re
from gginfo import items

class YzmuseumSpider(scrapy.Spider):
    name = 'yzmuseum'
    # allowed_domains = ['https://www.yzmuseum.com/website/treasure/detail.php?id=']
    # start_urls = ['http://https://www.yzmuseum.com/website/treasure/detail.php?id=/']

    def start_requests(self):
        start_page = 600
        end_page = 800
        base_url = "https://www.yzmuseum.com/website/treasure/detail.php?id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + ".html"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 47
        name = response.css('#content_body > div.tresure_detail_head::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#content_cover::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "https://www.yzmuseum.com"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(2, len(str(pic[-1]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('#content_text *::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\xa0', '')
            Items['text'] = s
        if Items['text'] == "":
            return
        yield Items
