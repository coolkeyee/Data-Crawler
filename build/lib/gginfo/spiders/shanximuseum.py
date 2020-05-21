# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class ShanximuseumSpider(scrapy.Spider):
    name = 'shanximuseum'
    # allowed_domains = ['http://www.shanximuseum.com/detail_collection/']
    # start_urls = ['http://http://www.shanximuseum.com/detail_collection//']

    def start_requests(self):
        start_page=300
        end_page=331
        base_url="http://www.shanximuseum.com/detail_collection/"
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
        Items['name']= response.css('body > div.x-container > div.collection_xx2 > div > div.x-tit.center > div.h18::text').extract()
        t= response.css('body > div.x-container > div.collection_xx2 > div > div.padd > div.cont > div *::text').extract()
        s=""
        picurl="http://www.shanximuseum.com"
        text = str(response.body_as_unicode())
        pattern = re.compile('<img.*?src="(.*?)"');
        for i in t:
            s+= str(i).strip()
        Items['text']=s
        Items['pic']=picurl+pattern.findall(text)[3]
        yield Items
