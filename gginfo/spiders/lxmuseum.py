# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items
class LxmuseumSpider(scrapy.Spider):
    name = 'lxmuseum'
    # allowed_domains = ['http://www.luxunmuseum.com.cn/html/']
    # start_urls = ['http://http://www.luxunmuseum.com.cn/html//']

    def start_requests(self):
        firstpage=["201507","201107","201509"]
        start_page=1179
        end_page=1207
        base_url = "http://www.luxunmuseum.com.cn/html/"
        count = 0
        for item in firstpage:

            for i in range(start_page, end_page):
                url = base_url + str(item)+'/'+'a'+str(i)+".htm"
                count += 1
                yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = response.meta['id']
        Items['name'] = response.css('body > div.main > div.main_r.r > div.main_content > div.content_title::text').extract()[0]
        t = response.css('body > div.main > div.main_r.r > div.main_content > div:nth-child(3) > div:nth-child(2) *::text').extract()
        s = ""
        picurl = "www.luxunmuseum.com.cn/"
        for item in t:
            item=str(item).strip()
            s+=item.replace('\u3000', '')
        Items['text'] = s
        Items['pic'] = picurl + str(response.css('body > div.main > div.main_r.r > div.main_content > div:nth-child(3) > div:nth-child(1) > img::attr(src)').extract()[0])
        yield Items
