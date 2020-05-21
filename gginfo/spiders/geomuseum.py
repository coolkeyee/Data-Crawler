# -*- coding: utf-8 -*-
import scrapy
from gginfo import items
import bs4
import re

class GeomuseumSpider(scrapy.Spider):
    name = 'geomuseum'
    # allowed_domains = ['http://www.gmc.org.cn/detail/']
    # start_urls = ['http://http://www.gmc.org.cn/detail//']

    def parse(self, response):
        pass
    def start_requests(self):
        start_page=500
        end_page=677
        base_url="http://www.gmc.org.cn/detail/"
        count=0
        for i in range(start_page,end_page):
            url=base_url+str(i)
            count+=1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id':count})
    def parse(self, response):
        if(response.status=='404'):
            return
        Items = items.GginfoItem()
        Items['id']= response.meta['id']
        Items['name']= response.css('body > div.x-container > div > div.col1 > div > div.r > div.t28::text').extract()[0]
        s=""
        for item in response.css('body > div.x-container > div > div.col1 > div > div.r *::text').extract():
            s+=str(item).strip()
        picurl="www.gmc.org.cn"
        Items['text']=s
        Items['pic']=""
        yield Items
