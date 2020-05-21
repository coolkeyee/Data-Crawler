# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class WhmSpider(scrapy.Spider):
    name = 'whm'
    # allowed_domains = ['http://www.whmuseum.com.cn/collection/ceramics']
    # start_urls = ['http://http://www.whmuseum.com.cn/collection/ceramics/']

    def start_requests(self):
        base_url = "http://www.whmuseum.com.cn/collection/ceramics"
        count = 0
        url = base_url + str(i) + ".html"
        count += 1
        yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if(response.status =='404'):
            return
        data=[]
        data=response.css('')

    def detailparse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 75
        name = response.css(
            'body > div.n_collection_box > ul > div.n_collection_con_box > li.n_collection_con_box_t > span::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > div.n_collection_box > ul > div.p_solid > ul > li > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.hnzzmuseum.com"
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css(
            'body > div.n_collection_box > ul > div.n_collection_con_box > li.n_collection_con_box_c *::text').extract()
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
