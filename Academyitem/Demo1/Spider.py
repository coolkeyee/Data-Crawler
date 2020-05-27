#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Joshua
@description:
    一个spider开一个浏览器
"""
import logging
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumSpider(scrapy.Spider):
    """
    Selenium专用spider

    一个spider开一个浏览器

    浏览器驱动下载地址:http://www.cnblogs.com/qiezizi/p/8632058.html
    """
    SetHeadless = False
    # 是否允许浏览器使用cookies
    EnableBrowserCookies = True

    def __init__(self, *args, **kwargs):
        super(SeleniumSpider, self).__init__(*args, **kwargs)
        # 获取浏览器操控权
        self.browser = self._get_browser()

    def _get_browser(self):
        """
        返回浏览器实例
        """
        # 设置selenium与urllib3的logger的日志等级为ERROR
        # 如果不加这一步，运行爬虫过程中将会产生一大堆无用输出
        logging.getLogger('selenium').setLevel('ERROR')
        logging.getLogger('urllib3').setLevel('ERROR')
        # selenium已经放弃了PhantomJS，开始支持firefox与chrome的无头模式
        return self._use_Chrome()

    def _use_Chrome(self):
        """
        使用selenium操作火狐浏览器
        """
        options = webdriver.ChromeOptions()
        # 下面一系列禁用操作是为了减少selenium的资源耗用，加速scrapy
        # 禁用图片
        # prefs = {
        #     'profile.default_content_setting_values': {
        #         'notifications': 2
        #     }
        # }
        # options.add_experimental_option('prefs', prefs)
        # 如果EnableBrowserCookies的值设为False，那么禁用cookies
        if self.SetHeadless:
            # 无头模式，无UI
            options.add_argument('-headless')
        # 禁用gpu加速
        # options.add_argument('--disable-gpu')
        # 禁用插件
        # options.add_argument('--disable-plugins')
        options = Options()
        options.headless = True
        return webdriver.Chrome(chrome_options=options)

    def selenium_func(self, request):
        """
        在返回浏览器渲染的html前做一些事情
            1.比如等待浏览器页面中的某个元素出现后，再返回渲染后的html；
            2.比如将页面切换进iframe中的页面；

        在需要使用的子类中要重写该方法，并利用self.browser操作浏览器
        """
        pass
