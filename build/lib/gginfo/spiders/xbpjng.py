# -*- coding: utf-8 -*-
import scrapy
import scrapy
import bs4
import re
from gginfo import items

class XbpjngSpider(scrapy.Spider):
    name = 'xbpjng'
    # allowed_domains = ['http://www.xbpjng.cn/wenbotiandi/shuhua.aspx?page=1']
    # start_urls = ['http://http://www.xbpjng.cn/wenbotiandi/shuhua.aspx?page=1/']

    def start_requests(self):
        start_page=1
        end_page=5
        base_url="http://www.xbpjng.cn/wenbotiandi/shuhua.aspx?page="
        count=0
        for i in range(start_page,end_page):
            url=base_url+str(i)
            count+=1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id':count})
    def parse(self, response):
        if(response.status=='404'):
            return
        detailurl=[]
        detailurl=response.css('#main > div.right_detail > div.zygg > div.i-list > ul > li > a::attr(href)').extract()
        for baseurl in detailurl:
            url='http://www.xbpjng.cn/wenbotiandi/'+baseurl
            yield scrapy.Request(url=url, callback=self.detailparse, meta={'id': response.meta['id']})
    def detailparse(self, response):
        if(response.status=='404'):
            return
        Items=items.GginfoItem()
        Items['id']=response.meta['id']
        Items['name'] = response.css('#ctl00_ContentPlaceHolder1_lb_Title::text').extract()[0]
        Items['pic']=response.css('#ctl00_ContentPlaceHolder1_lb_Content > img::attr(src)').extract()[0]
        Items['text']="无详细内容"
        yield Items
