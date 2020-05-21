#-*- codeing =utf-8 -*-
#@ Time : 2020/5/17 15:42
#@Author : 林鑫
#@File : main.py
#@Software: PyCharm
from scrapy import cmdline
# name ='info'
# name = 'geomuseum'
# name = 'lxmuseum'
# name = 'capitalmuseum'
# name = 'gqwmuseum'
# name = 'tjmuseum'
# name = 'xbpjng'
# name = 'shanximuseum'
# name = 'balujun'
# name = 'lnmuseum'
# name = 'lvshunmuseum'
# name = 'sypm'
# name = 'wmhg'
# name = 'aihui'
# name = 'daqing'
# name = 'shmuseum'
# name = 'cyjng'
# name = 'yzmuseum'
# name = 'njmuseum'
# name = 'silk'
# name = 'hzmuseum'
# name = 'wzmuseum'
# name = 'ahm'
# name = 'gtm'
# name = 'jgsm'
# name = 'jxm'
# name = 'rjjng'
# name = 'aym'
# name = 'qdm'
# name = 'sdm'
# name = 'hnzz'
# name = 'kfsm'
name = '1991m'
cmd = 'scrapy crawl {0}{1}'.format(name,'')
cmdline.execute(cmd.split())