# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GginfoItem(scrapy.Item):
    # define the fields for your item here like:
    id =scrapy.Field()
    name = scrapy.Field()
    pic=scrapy.Field()
    text=scrapy.Field()
