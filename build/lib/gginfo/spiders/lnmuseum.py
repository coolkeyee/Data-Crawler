# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items



class LnmuseumSpider(scrapy.Spider):
    name = 'lnmuseum'
    # allowed_domains = ['http://www.lnmuseum.com.cn/huxing/show.asp?id=']
    # start_urls = ['http://http://www.lnmuseum.com.cn/huxing/show.asp?id=/']

    def start_requests(self):
        start_page = 6500
        end_page = 6700
        base_url = "http://www.lnmuseum.com.cn/huxing/show.asp?id="
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 26
        name = response.css('body > table:nth-child(3) > tr:nth-child(2) > td > table > tr > td:nth-child(4) > table > tr:nth-child(3) > td > table > tr:nth-child(4) > td > p:nth-child(2)::text').extract()
        if len(name) == 0:
            return
        Items['name'] = str(str(name[0]).strip()).replace('\xa0', '')
        if(Items['name']==""):
            return
        t = response.css('body > table > tr > td > table > tr > td > table > tr > td > table > tr > td *::text').extract()
        # s = response.css('#dui > div > a::attr(src)').extract()
        text = str(response.body_as_unicode())
        pattern = re.compile('<img.*?src="(.*?)"');
        # if len(s) == 0:
        #     s = response.css('body > table > tr > td > table > tr > td > table > tr > td > table > tr > td *::text').extract()
        #     if len(s) == 0:
        #         return
        picurl = "http://www.lnmuseum.com.cn"
        s=""
        if len(t)==0:
            Items['text'] = "无详细介绍"
        else:
            for i in range(27, len(t)-6):
                s+=str(str(t[i]).strip()).replace('\xa0', '')
            Items['text']=s
        s1=pattern.findall(text)[-4]
        s2=""
        for i in range(len(s1)):
            if(s1[i]!='/'):
                pass
            else:
                for j in range(i,len(s1)):
                    s2+=s1[j]
                break
        Items['pic'] = picurl + s2
        yield Items

