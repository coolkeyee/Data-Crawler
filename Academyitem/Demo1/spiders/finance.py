# -*- coding: utf-8 -*-
import scrapy
from Demo1.items import academyItem
import Demo1.spiders.finance_config as Config
import os
from selenium import webdriver
from Demo1.Request import SeleniumRequest
from Demo1.Spider import SeleniumSpider
from Demo1.Tools import waitForCss
import json


class VisSpider(SeleniumSpider):
    name = 'finance'
    father_css = str()

    def start_requests(self):
        for i in range(len(Config.URL)):
            # 测试用, 清空txt文件
            path_str = 'education_txt/' + str(Config.parse_parameter[i]['mid']) + '.txt'
            if os.access(path_str, os.F_OK) is True:
                f = open(path_str, "r+")
                f.truncate()

            url_str = Config.URL[i]
            if Config.URL_method[i] == 0:  # GET请求
                self.father_css = Config.parse_parameter[i]['father']
                for j in Config.URL_page[i]:
                    new_url_str = url_str + j
                    yield SeleniumRequest(url=new_url_str, callback=lambda response,
                                          message=Config.parse_parameter[i]: self.parse_get(response, message))
            else:  # POST请求
                for j in Config.URL_page[i]:
                    new_url_str = url_str + j
                    yield scrapy.Request(url=new_url_str,
                                     method='POST', callback=lambda response, message=Config.parse_parameter[i]:
                                     self.parse_post(response, message))

    def parse_get(self, response, message):  # GET请求分析
        father = response.css(message['father'])  # 找到模块的父节点
        names = father.css(message['name']).extract()  # 找到名字
        urls = father.css(message['url']).extract()  # 找到url
        for i in range(len(names)):
            names[i] = names[i].strip()
        for i in range(len(urls)):  # 更新url, 即头部加上官网网址
            if urls[i][0].isalpha() is False:  # 删除开头的.
                while urls[i][0].isalnum() is False:
                     urls[i] = urls[i][1:]
                urls[i] = message['rootUrl'] + '/' + urls[i]
            else:
                if 'http' not in urls[i]:
                    urls[i] = message['rootUrl'] + urls[i]
        with open('education_txt/' + str(message['mid']) + '.txt', 'a', encoding='utf-8') as f:  # 测试, 写入文件
            for i in range(len(names)):
                f.write('name: ' + names[i] + '\n')
                f.write('url: ' + urls[i] + '\n')
                f.write('\n')
            f.write('\n\n')

        for i in range(len(names)):
            item = academyItem()
            item['mid'] = message['mid']
            item['name'] = names[i]
            item['url'] = urls[i]
            yield item

    def parse_post(self, response, message):  # POST请求分析
        json_txt = json.loads(response.text)
        for i in message['father']:
            json_txt = json_txt[i]
        names = []
        urls = []
        for i in json_txt[message['list']]:
            names.append(i[message['title']])  # 加入标题

            if isinstance(message['url'], dict):
                url_str = ''                # 根据参数合成url
                order = message['order']
                for j in range(len(order)):
                    value = ''
                    if message['url'][order[j]] == '':
                        key = message['json_url'][order[j]]
                        value = i[key]
                    else:
                        value = message['url'][order[j]]
                    value = order[j] + '=' + str(value)
                    if j < len(order) - 1:
                        value = value + '&'
                    url_str = url_str + value
            else:
                url_str = i[message['url']]

            urls.append(message['rootUrl'] + url_str)  # 加入url

        with open('education_txt/' + str(message['mid']) + '.txt', 'a', encoding='utf-8') as f:  # 测试, 写入文件
            for i in range(len(names)):
                f.write('name: ' + names[i] + '\n')
                f.write('url: ' + urls[i] + '\n')
                f.write('\n')
            f.write('\n\n')

        for i in range(len(names)):
            item = academyItem()
            item['mid'] = message['mid']
            item['name'] = names[i]
            item['url'] = urls[i]
            yield item

    def selenium_func(self, request):
        # 这个方法会在我们的下载器中间件返回Response之前被调用

        # 等待content内容加载成功后，再继续
        # 这样的话，我们就能在parse_content方法里应用选择器扣出#content了
        waitForCss(self.browser, self.father_css)

