# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class SilkSpider(scrapy.Spider):
    name = 'silk'
    # allowed_domains = ['http://www.chinasilkmuseum.com/zggd/info_21.aspx?itemid=']
    # start_urls = ['http://http://www.chinasilkmuseum.com/zggd/info_21.aspx?itemid=/']

    def start_requests(self):
        start_page = 3100
        end_page = 3300
        base_url = "http://www.chinasilkmuseum.com/zggd/info_21.aspx?itemid="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 52
        name = response.css('body > div.about > div > div.about_body > div > div.detail_head > div.detail_h::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > div.about > div > div.about_body > div > div.detail_text > a > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.chinasilkmuseum.com"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[-1]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('div.detail_text::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\u3000', '')
            Items['text'] = s.replace('\xa0','')
        if Items['text'] == "":
            return
        yield Items
