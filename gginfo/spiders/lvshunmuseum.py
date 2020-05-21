# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class LvshunmuseumSpider(scrapy.Spider):
    name = 'lvshunmuseum'
    # allowed_domains = ['http://www.lvshunmuseum.org/collection/ProductDetail.aspx?ID=']
    # start_urls = ['http://http://www.lvshunmuseum.org/collection/ProductDetail.aspx?ID=/']

    def start_requests(self):
        start_page = 50
        end_page = 100
        base_url = "http://www.lvshunmuseum.org/collection/ProductDetail.aspx?ID="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 28
        name=response.css('#showcasescontent > div > div.ps_text > h1::text').extract()
        if(len(name)==0):
            return
        Items['name']=name[0]
        pic=response.css('#showcasescontent > div > div.pictureshow > li > img::attr(src)').extract()
        if(len(pic)==0):
            return
        base_url="http://www.lvshunmuseum.org"
        url=base_url+str(pic[0]).strip()
        Items['pic']=url
        text=response.css('#showcasescontent > div > div.textshow > p::text').extract()
        if(len(text)==0):
            Items['text']=""
        else:
            s=""
            for item in text:
               s+=str(str(item).strip()).replace('\xa0','')
            Items['text']=s
        yield Items
