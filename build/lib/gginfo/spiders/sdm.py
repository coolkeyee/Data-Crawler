# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class SdmSpider(scrapy.Spider):
    name = 'sdm'
    # allowed_domains = ['http://www.sdmuseum.com/channels/ch00079/']
    # start_urls = ['http://http://www.sdmuseum.com/channels/ch00079//']

    def start_requests(self):
        url = "http://www.sdmuseum.com/channels/ch00079/"
        count = 0
        yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        detailurl = []
        # detailurl = response.css('div.cp-pic > a::attr(href)').extract()

        for baseurl in detailurl:
            url = 'http://www.gthyjng.com/gcww/wwjs/tdgmsq/' + baseurl
            yield scrapy.Request(url=url, callback=self.detailparse, meta={'id': response.meta['id']})

    def detailparse(self, response):
        if (response.status == '404'):
            return
        # Items = items.GginfoItem()
        # Items['id'] = 59
        # name = response.css('body > div.con.pad_t25 > div > div.xl > div.xl_top > h1::text').extract()
        # if (len(name) == 0):
        #     return
        # Items['name'] = str(name[0]).strip()
        # pic = response.css('img::attr(src)').extract()
        # if (len(pic) == 0):
        #     return
        # base_url = response.url
        # pos = 0
        # url = ""
        # for i in range(len(base_url)):
        #     if base_url[i] == '/':
        #         pos = i
        # for i in range(0, pos):
        #     url += base_url[i]
        # pic1 = str(pic[-8]).strip()
        # pic2 = ""
        # for i in range(1, len(str(pic[-8]).strip())):
        #     pic2 += pic1[i]
        # url += pic2
        # Items['pic'] = url
        # text = response.css('#fontzoom > div > div:nth-child(2) > font::text').extract()
        # if (len(text) == 0):
        #     Items['text'] = ""
        # else:
        #     s = ""
        #     for item in text:
        #         s += str(str(item).strip()).replace('\u3000', '')
        #     Items['text'] = s.replace('\xa0', '')
        # yield Items
