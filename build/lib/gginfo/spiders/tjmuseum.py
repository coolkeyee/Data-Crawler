# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class TjmuseumSpider(scrapy.Spider):
    name = 'tjmuseum'
    # allowed_domains = ['https://www.tjbwg.com/cn/collectionInfo.aspx?Id=']
    # start_urls = ['http://https://www.tjbwg.com/cn/collectionInfo.aspx?Id=/']

    def start_requests(self):
        start_page = 2315
        end_page = 2389
        base_url = "https://www.tjbwg.com/cn/collectionInfo.aspx?Id="
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
        Items['name'] = str(response.css('body > div > div.main > div > div > div.collD.clearfix > div.collD_con > div.collD_cc > div.collD_h > h3::text').extract()[0]).strip()
        t = response.css('body > div > div.main > div > div > div.collD.clearfix > div.collD_con > div.collD_cc > div.d_con *::text').extract()
        s = ""
        text=str(response.body_as_unicode())
        pattern = re.compile('<img.*?src="(.*?)"');
        for item in pattern.findall(text):
            print(item)
        # print(text)
        # picurl = "https://img.dpm.org.cn/"
        for i in range(len(t)):
            s += str(t[i]).strip()
        Items['text'] = s
        Items['pic'] = pattern.findall(text)[1]
        yield Items

