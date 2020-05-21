# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class AihuiSpider(scrapy.Spider):
    name = 'aihui'
    # allowed_domains = ['http://www.aihuihistorymuseum.org.cn/concon.aspx?id=']
    # start_urls = ['http://http://www.aihuihistorymuseum.org.cn/concon.aspx?id=/']

    def start_requests(self):
        start_page = 1100
        end_page = 1500
        base_url = "http://www.aihuihistorymuseum.org.cn/concon.aspx?id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 35
        name = response.css('#ContentPlaceHolder1_title::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('#ContentPlaceHolder1_content > p > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = "https://www.wmhg.com.cn"
        url = base_url + str(pic[0]).strip()
        Items['pic'] = url
        text = response.css('ContentPlaceHolder1_content > p *::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\xa0', '')
            Items['text'] = s
        yield Items