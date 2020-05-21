# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items

class BalujunSpider(scrapy.Spider):
    name = 'balujun'
    # allowed_domains = ['http://www.balujun.cn/e/action/ShowInfo.php?classid=45&id=']
    # start_urls = ['http://http://www.balujun.cn/e/action/ShowInfo.php?classid=45&id=/']

    def start_requests(self):
        start_page = 1679
        end_page = 1721
        base_url = "http://www.balujun.cn/e/action/ShowInfo.php?classid=46&id="
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
        name=response.css('#home > div > div > div > div.content > div.content-title > h3::text').extract()
        if len(name)==0:
            return
        Items['name'] =name[0]
        t = response.css('div.content_edit *::text').extract()
        s = response.css('#vsb_content > div > div > img::attr(src)').extract()
        if len(s)==0:
            s=response.css('#vsb_content > div > p > img::attr(src)').extract()
            if len(s)==0:
                return
        picurl = "http://www.balujun.cn"
        Items['text'] = "无详细介绍"
        Items['pic'] = picurl + str(s[0])
        yield Items
