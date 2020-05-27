# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from twisted.internet import defer, threads
from Demo1.Request import SeleniumRequest
from Demo1.Spider import SeleniumSpider


class Demo1SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Demo1DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        # 如果spider为SeleniumSpider的实例，并且request为SeleniumRequest的实例
        # 那么该Request就认定为需要启用selenium来进行渲染html
        if isinstance(spider, SeleniumSpider) and isinstance(request, SeleniumRequest):
            # 控制浏览器打开目标链接
            spider.browser.get(request.url)

            # 在构造渲染后的HtmlResponse之前，做一些事情
            # 1.比如等待浏览器页面中的某个元素出现后，再返回渲染后的html；
            # 2.比如将页面切换进iframe中的页面；
            spider.selenium_func(request)

            # 获取浏览器渲染后的html
            html = spider.browser.page_source

            # 构造Response
            # 这个Response将会被你的爬虫进一步处理
            return HtmlResponse(url=spider.browser.current_url, request=request, body=html.encode(), encoding="utf-8")

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# class JavaScriptMiddleware(object):
#     def __init__(self):
#         self.timeout = 50
#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless')
#         self.browser = webdriver.Chrome(chrome_options=options)
#
#     def process_request(self, request, spider):
#         # executable_path = '/home/hadoop/crawlcompanyinfo0906/phantomjs'
#         # print"PhantomJS is starting..."
#         # driver = webdriver.PhantomJS(executable_path)  # 指定使用的浏览器
#         if self.browser.current_url != request.url:
#             # 获取页面
#             self.browser.get(request.url)
#             time.sleep(5)
#         else:
#             pass
#         time.sleep(5)
#         print ("访问" + request.url)
#         return HtmlResponse(self.browser.current_url, body=self.browser.page_source, encoding='utf-8', request=request)
#
#     def spider_closed(self):
#         # 爬虫结束 关闭窗口
#         self.browser.close()
#         pass
