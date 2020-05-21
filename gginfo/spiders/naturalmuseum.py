# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items
class NaturalmuseumSpider(scrapy.Spider):
    name = 'naturalmuseum'
    # allowed_domains = ['http://www.bmnh.org.cn/gzxx/gzbb/11/list_2.shtml']
    # start_urls = ['http://http://www.bmnh.org.cn/gzxx/gzbb/11/list_2.shtml/']

    def start_requests(self):
        start_page = 2
        end_page = 9
        base_url = "http://www.bmnh.org.cn/gzxx/gzbb/"
        count = 0
        for x in range(11,20):
            for i in range(start_page, end_page):
                url = base_url + str(x)+"/list_"+str(i)+".shtml"
                count += 1
                yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = response.meta['id']
        pic=[]
        pic=response.css('body > div.content_normal > div.content_shop > div.content_shopr > div.row.shopList.col_list > div > div > a > img::attr(src)').extract()
        name=[]
        name=response.css('body > div.content_normal > div.content_shop > div.content_shopr > div.row.shopList.col_list > div > div > a > img::attr(alt)').extract()
        for i in range(len(pic)):
            Items['text']="无"
            Items['name']=name[i]
            Items['pic']="http://www.bmnh.org.cn"+pic[i]
            yield Items
