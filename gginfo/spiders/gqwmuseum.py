# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class GqwmuseumSpider(scrapy.Spider):
    name = 'gqwmuseum'
    # allowed_domains = ['http://www.pgm.org.cn/newPgm_Collection/findCollectById?collect.id=']
    # start_urls = ['http://http://www.pgm.org.cn/newPgm_Collection/findCollectById?/']

    def start_requests(self):
        start_page = 6666
        end_page = 8888
        base_url = "http://www.pgm.org.cn/newPgm_Collection/findCollectById?collect.id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = response.meta['id']
        s=[]
        s=response.css('body > div > div > table > tr> td:nth-child(2)::text').extract()
        if len(s)==0:
            return
        Items['name'] = s[0]
        t = response.css('body > div > div > table >tr:nth-child(3) > td:nth-child(2)::text').extract()[0]
        picurl = "http://www.pgm.org.cn"
        Items['text'] = str(t).strip()
        Items['pic'] = picurl + str(response.css('body > div > div > table > tr:nth-child(1) > td:nth-child(3) > img::attr(src)').extract()[0])
        yield Items

