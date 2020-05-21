# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items
class InfoSpider(scrapy.Spider):
    name = 'capitalmuseum'
    # allowed_domains = ['www.dpm.org.cn/collection/ceramic/']
    # start_urls = ['http://www.dpm.org.cn/collection/ceramic//']
    def start_requests(self):
        start_page=226704
        end_page=227204
        url="https://baike.baidu.com/item/%E9%A6%96%E9%83%BD%E5%8D%9A%E7%89%A9%E9%A6%86"
        count=0
        yield scrapy.Request(url=url, callback=self.parse, meta={'id':count})
    def parse(self, response):
        if(response.status=='404'):
            return
        Items = items.GginfoItem()
        Items['id']= response.meta['id']
        data=[]
        name=[]
        text=[]
        data=response.css('body > div.body-wrapper > div.content-wrapper > div > div.main-content > table > tr > td::text').extract()
        print(data)
        flag = True
        s1=""
        for i in range(len(data)) :
            if i<3:
                continue
            s=str(data[i]).strip()
            if(len(s)>0 and len(s)<=8):
                if(flag):
                    flag = False
                else:
                    text.append(s1)
                    s1=""
                name.append(s)
            elif(len(s)>8):
                s1+=s
        for i in range(min(len(name),len(text))):
            print(name[i])
            print(text[i])
        picurl=[]
        picurl=response.css('body > div > div > div > div > table > tr > td > div > div > a::attr(href)').extract()
        exp=3
        for i in range(-1+min(len(text),len(name),len(picurl))-1):
           Items['name']=name[i+1]
           Items['text']=text[i+1]
           Items['pic']="https://baike.baidu.com"+picurl[i+exp]
           if(i==4):
               exp=4
           yield Items
