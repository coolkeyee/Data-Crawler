# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items
class InfoSpider(scrapy.Spider):
    name = 'info'
    # allowed_domains = ['www.dpm.org.cn/collection/ceramic/']
    # start_urls = ['http://www.dpm.org.cn/collection/ceramic//']
    def start_requests(self):
        start_page=226704
        end_page=227204
        base_url="http://www.dpm.org.cn/collection/ceramic/"
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
        Items['name']= response.css('h3 span::text').extract()[0]
        t= response.css('div.content_edit *::text').extract()
        s=""
        picurl="https://img.dpm.org.cn/"
        for i in range(len(t)-1):
            s+= str(t[i]).replace('\u3000', '')
        Items['text']=s
        Items['pic']=picurl+str(response.css('div.pic img::attr(src)').extract()[0])
        yield Items




