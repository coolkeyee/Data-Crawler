# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class CyjngSpider(scrapy.Spider):
    name = 'cyjng'
    # allowed_domains = ['http://www.cyjng.net/Default.aspx?tabid=62&language=zh-CN']
    # start_urls = ['http://http://www.cyjng.net/Default.aspx?tabid=62/']

    def start_requests(self):
        start_page = 1
        end_page = 2
        base_url = "http://www.cyjng.net/Default.aspx?tabid=62&language=zh-CN"
        count = 0
        for i in range(start_page, end_page):
            url = base_url
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        detailurl = []

        for baseurl in detailurl:
            url = 'http://www.cyjng.net' + baseurl
            yield scrapy.Request(url=url, callback=self.detailparse, meta={'id': response.meta['id']})

    def detailparse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 42
        name = response.css('#dnn_ctr504_ArticleDetails_ctl00_lblTitle::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#dnn_ctr504_ArticleDetails_ctl00_imgArticleImage::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "http://www.cyjng.net"
        url = base_url + str(pic[0]).strip()
        Items['pic'] = url
        text = response.css('#dnn_ctr504_ArticleDetails_ctl00_lblArticle > p::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\xa0', '')
            Items['text'] = s
        yield Items
