# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class SypmSpider(scrapy.Spider):
    name = 'sypm'
    # allowed_domains = ['http://www.sypm.org.cn/products_detail3/productId=']
    # start_urls = ['http://http://www.sypm.org.cn/products_detail3/productId=/']

    def start_requests(self):
        start_page = 100
        end_page = 200
        base_url = "http://www.sypm.org.cn/products_detail3/productId="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)+".html"
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 29
        name = response.css('#FrontProducts_detail02-0012_subm > div.content > div.pro-module > ul.basic > li::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#FrontProducts_detail02-0012_bigImg::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.lvshunmuseum.org"
        url = base_url + str(pic[0]).strip()
        Items['pic'] = url
        text = response.css('#FrontProducts_detail02-0012_cont_1::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\xa0', '')
            Items['text'] = s
        yield Items
