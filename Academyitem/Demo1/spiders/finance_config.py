URL = [
       'https://www.dpm.org.cn/learning/dynamic/p/',  # 故宫博物馆
       'http://www.gmc.org.cn/researchdynamic/p/',    # 中国地质博物馆
       'http://www.jb.mil.cn/yjcz_2226/gbtg/index',  # 中国人民革命军事博物馆
       'http://www.luxunmuseum.com.cn/xueshuyanjiu/list_18_',  # 北京鲁迅博物馆
       'http://www.capitalmuseum.org.cn/xsyj/',  # 首都博物馆
       'http://www.bmnh.org.cn/kxyj/',  # 北京自然博物馆
       'http://www.1937china.com/rest/business/kzslw/xsyjXsdt/list?',  # 中国人民抗日战争纪念馆
       'http://www.zkd.cn/kxyj2/index',  # 周口店猿人遗址博物馆
       'http://www.chnmuseum.cn/yj/xscg/xslw/index',  # 中国国家博物馆
       'http://www.ciae.com.cn/searchs/digital/lang/zh/category_id/30/tpl_file/digital/linkage_id/0/p/',  # 中国农业博物馆
       'http://www.pgm.org.cn/pgm/xsyjou/list',  # 文化部恭王府博物馆
       'https://www.tjbwg.com/cn/News.aspx?',  # 天津博物馆
       'https://www.tjnhm.com/index.php?p=kxyj&lanmu=4&c_id=15&',  # 天津自然博物馆
       'http://www.xbpjng.cn/News/NewsList_New.aspx?id=ac3022bd-d56f-4778-b2f5-97217edea99e&',  # 西柏坡纪念馆
       'http://www.hdmuseum.org/newslist.asp?',  # 邯郸市博物馆
       'http://www.shanximuseum.com/research/paper/p/',  # 山西博物院
       'http://www.coalmus.org.cn/html/list_1650',  # 中国煤炭博物馆
       'http://www.balujun.cn/e/action/ListInfo/index.php?',  # 八路军太行纪念馆
       'http://www.nmgbwy.com/xsyj/index',  # 内蒙古博物院
       'http://www.lnmuseum.com.cn/yanjiu/?',  # 辽宁省博物馆
       'http://www.lvshunmuseum.org/Academic/default.aspx?',  # 旅顺博物馆
       'http://www.sypm.org.cn/news_list2/newsCategoryId=',     # 沈阳故宫博物院
       'http://www.jlmuseum.org/learning/',   # 吉林省博物院
       'https://www.wmhg.com.cn/achievements/p/',    # 伪满皇宫博物院
       'http://www.hljmuseum.com/',    # 黑龙江省博物馆
       'https://www.shanghaimuseum.net/museum/frontend/research/research.action?researchTypeCode=CATALOG',  # 上海博物馆
       'http://www.cyjng.net/Default.aspx?tabid=81&',  # 陈云纪念馆
       'http://www.njmuseum.com/api/news/list?',    # 南京博物院
       'http://www.19371213.com.cn/research/publications/',    # 侵华日军南京大屠杀遇难同胞纪念馆
       'http://www.ntmuseum.com/colunm6/col5/list_36_',    # 南通博物苑
       'https://www.yzmuseum.com/website/research/achievement.php?',   # 扬州博物馆
]

# URL的分页信息
URL_page = [
        [('%s.html' % i) for i in range(1, 4)],
        [('%s.html' % i) for i in range(1, 5)],
        ['.html']+[('_%s.html' % i) for i in range(1, 3)],
        [('%s.htm' % i) for i in range(1, 4)],
        ['kgxlz.htm', 'kgfjbg.htm', 'kgfjbg_2.htm', 'sxyj.htm', 'sxyj_2.htm', 'sxyj_3.htm'],
        ['kycg/list.shtml', 'xshd/list.shtml', 'xshd/list_2.shtml'],
        ['status=0&pageSize=10&pageNum=1', 'status=0&pageSize=10&pageNum=2', 'status=0&pageSize=10&pageNum=3'],
        ['.jhtml', '_2.jhtml'],
        ['.shtml', '_1.shtml', '_2.shtml'],
        ['1.html'],
        ['.shtml', '_2.shtml'],
        ['current=1&TypeId=10950', 'current=2&TypeId=10950', 'current=3&TypeId=10950'],
        ['page=1', 'page=2', 'page=3'],
        ['page=1', 'page=2', 'page=3'],
        ['cd=53'],
        ['1.html?0.014455018788368745', '2.html?0.7134114268706448', '3.html?0.7221064631791161', '4.html?0.3391611491019022'],
        ['.html', '_2.html'],
        ['page=0&classid=18', 'page=1&classid=18', 'page=2&classid=18'],
        ['.jhtml?contentId=170', '_2.jhtml?contentId=170', '_3.jhtml?contentId=170'],
        ['Page=1&ChannelID=466', 'Page=2&ChannelID=466'],
        ['SortID=6&Page=1', 'SortID=6&Page=2'],
        ['74.html', '13.html'],
        ['', '2.html'],
        ['1.html?0.9620169164315724', '2.html?0.03056076108622574', '3.html?0.5691053122954195', '4.html?0.9372993040233752'],
        ['xskj/ttyjl/index.html', 'system/more/xskj/ttyjl/index/page_01.html', 'xskj/ktyj/'],
        [''],
        ['currentpage=1&language=zh-CN', 'currentpage=2&language=zh-CN', 'currentpage=3&language=zh-CN'],
        ['pageNum=1&pageSize=10&typeValue=7&modular=scientific', 'pageNum=2&pageSize=10&typeValue=7&modular=scientific'],
        ['index.html', 'index_1.html', 'index_2.html'],
        ['1.html', '2.html'],
        ['page=1', 'page=2'],
]

URL_method = [  # 请求方法, 0--GET, 1--POST
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
]


# 在parse函数里用到的信息
parse_parameter = [
    {'mid': 1,  # 故宫博物馆
     'rootUrl': 'www.dpm.org.cn',
     'father': '#lists > ul',
     'name': 'h1 > a::text',
     'url': 'h1 > a::attr(href)'
     },

    {'mid': 3,  # 中国地质博物馆
     'rootUrl': 'www.gmc.org.cn',
     'father': '#datalist > div.con2',
     'name': 'a > div.ll > div.t18::text',
     'url': 'a::attr(href)'
     },

    {'mid': 4,  # 中国人民革命军事博物馆
     'rootUrl': 'www.jb.mil.cn/yjcz_2226/gbtg',
     'father': 'body > div.main > div.infoDynamicList > ul',
     'name': 'a > h3::text',
     'url': 'a::attr(href)'
     },

    {'mid': 6,  # 北京鲁迅博物馆
     'rootUrl': 'www.luxunmuseum.com.cn',
     'father': 'body > div.main > div.main_r.r > div.main_content > div.content_czyd',
     'name': 'div.list_l.l > dt > a::text',
     'url': 'div.list_l.l > dt > a::attr(href)'
     },

    {'mid': 7,  # 首都博物馆
     'rootUrl': 'www.capitalmuseum.org.cn/xsyj/',
     'father': '#__01 > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table:nth-child(2) > tbody > tr > td:nth-child(3)',
     'name': 'tbody > tr:nth-child(1) > td > a::text',
     'url': 'tbody > tr:nth-child(1) > td > a::attr(href)'
     },

    {'mid': 8,  # 北京自然博物馆
     'rootUrl': 'www.bmnh.org.cn',
     'father': 'body > div.content > div.content_sci > div.content_singler.singler_sci',
     'name': 'a > span::text',
     'url': 'a::attr(href)'
     },

    {'mid': 9,  # 中国人民抗日战争纪念馆
     'rootUrl': 'http://www.1937china.com/views/newsdetail/news_detail.html?',
     'father': [],
     'list': 'rows',
     'title': 'title',
     'url': {
         'id': '',
         'newsSession': 'xsyj_xsdt',
         'isTitleShow': 'true',
         'parentPage': 'xsyj_xsdt',
         'fileName': ''
        },
     'order': ['id', 'newsSession', 'isTitleShow', 'parentPage', 'fileName'],
     'json_url': {
         'id': 'id',
         'fileName': 'htmlFileName'
        },
     },

    {'mid': 10,  # 周口店猿人遗址博物馆
     'rootUrl': '',
     'father': 'body > div.main_bg > div > div.right_box > div.zlhg2_list > ul',
     'name': 'a::attr(title)',
     'url': 'a::attr(href)'
     },

    {'mid': 11,  # 中国国家博物馆
     'rootUrl': 'www.chnmuseum.cn/yj/xscg/xslw',
     'father': 'body > div.cj_ercom_wai.cj_fff > div > div > ul',
     'name': 'a:nth-child(2)::attr(title)',
     'url': 'a:nth-child(2)::attr(href)'
     },

    {'mid': 12,  # 中国农业博物馆
     'rootUrl': 'www.ciae.com.cn',
     'father': '#ajax-list > ul',
     'name': 'a::attr(title)',
     'url': 'a::attr(href)'
     },

    {'mid': 14,  # 文化部恭王府博物馆
     'rootUrl': 'www.pgm.org.cn',
     'father': 'body > div > div:nth-child(5) > div.bke4.p18.mb40 > ul',
     'name': 'a::attr(title)',
     'url': 'a::attr(href)'
     },

    {'mid': 15,  # 天津博物馆
     'rootUrl': 'www.tjbwg.com/cn/',
     'father': 'body > div > div.main > div > div > div.mainCon > div.mainC.plt0 > div > div > ul',
     'name': 'h3::text',
     'url': 'a::attr(href)'
     },

    {'mid': 16,  # 天津自然博物馆
     'rootUrl': 'www.tjnhm.com/',
     'father': '#news_content > ul',
     'name': 'a::text',
     'url': 'a::attr(href)'
     },

    {'mid': 19,  # 西柏坡纪念馆
     'rootUrl': 'http://www.xbpjng.cn/News/',
     'father': '#ctl00 > div.right_detail > div > div.all-content',
     'name': 'h2 > a::text',
     'url': 'h2 > a::attr(href)'
     },

    {'mid': 20,  # 邯郸市博物馆
     'rootUrl': 'http://www.hdmuseum.org/',
     'father': 'body > table:nth-child(9) > tbody > tr > td:nth-child(3) > table > tbody > tr > td > table:nth-child(2) > tbody > tr > td > table > tbody > tr > td.righttableborder > table > tbody > tr > td > table:nth-child(1) > tbody',
     'name': 'td:nth-child(1) > a::attr(title)',
     'url': 'td:nth-child(1) > a::attr(href)'
     },

    {'mid': 21,  # 山西博物院
     'rootUrl': 'http://www.shanximuseum.com',
     'father': '#datalist > div.list',
     'name': 'a > div > div.h18::text',
     'url': 'a::attr(href)'
     },

    {'mid': 22,  # 中国煤炭博物馆
     'rootUrl': '',
     'father': '#LB > ul',
     'name': 'a::text',
     'url': 'a::attr(href)'
     },

    {'mid': 23,  # 八路军太行纪念馆
     'rootUrl': 'http://www.balujun.cn',
     'father': '#home > div > div > div.main-right > div.list',
     'name': 'li > div > a > h3 > strong::text',
     'url': 'div.list-txt > a::attr(href)'
     },

    {'mid': 24,  # 内蒙古博物院
     'rootUrl': '',
     'father': 'body > div.container-fluid > div:nth-child(2) > div.col-sm-8.col-xs-10.col-xs-offset-1.col-sm-offset-2.col-md-offset-1.leftContent > div > div > div',
     'name': 'div.col-sm-8.col-xs-12.col-xs-offset-3 > div:nth-child(1) > a::text',
     'url': 'div.col-sm-8.col-xs-12.col-xs-offset-3 > div:nth-child(1) > a::attr(href)'
     },

    {'mid': 26,  # 辽宁省博物馆
     'rootUrl': 'www.lnmuseum.com.cn',
     'father': 'body > table:nth-child(2) > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(4) > table > tbody > tr:nth-child(3) > td > table:nth-child(1) > tbody',
     'name': 'td > table:nth-child(2) > tbody > tr > td > a::attr(title)',
     'url': 'td > table:nth-child(2) > tbody > tr > td > a::attr(href)'
     },

    {'mid': 28,  # 旅顺博物馆
     'rootUrl': 'http://www.lvshunmuseum.org',
     'father': '#tab > div > div > div.collection.acdmp > ul',
     'name': 'a > div.textbox > h1::text',
     'url': 'a::attr(href)'
     },

    {'mid': 29,  # 沈阳故宫博物院
     'rootUrl': 'http://www.sypm.org.cn',
     'father': '#FrontNews_list01-001 > ul',
     'name': 'a::attr(title)',
     'url': 'a::attr(href)'
     },

    {'mid': 31,  # 吉林省博物院
     'rootUrl': 'http://www.jlmuseum.org',
     'father': 'body > div.pub-page.clearfix.wrap > div.right > div.list-txt > ul',
     'name': 'a::attr(title)',
     'url': 'a::attr(href)'
     },

    {'mid': 32,  # 伪满皇宫博物院
     'rootUrl': 'http://www.jlmuseum.org',
     'father': '#datalist > div.list-box6',
     'name': 'div.cont > div.h18 > a::attr(title)',
     'url': 'div.cont > div.h18 > a::attr(href)'
     },

    {'mid': 36,  # 黑龙江省博物馆
     'rootUrl': 'http://www.hljmuseum.com',
     'father': '#erji-cent > div.erji-left.fl > ul',
     'name': 'a::text',
     'url': 'a::attr(href)'
     },

    {'mid': 38,  # 上海博物馆
     'rootUrl': 'https://www.shanghaimuseum.net',
     'father': '#research-list',
     'name': 'div.research-detail > div.research-name::text',
     'url': 'div.research-detail > div.research-footer > span:nth-child(1) > a::attr(href)'
     },

    {'mid': 42,  # 陈云纪念馆
     'rootUrl': 'http://www.cyjng.net',
     'father': '#dnn_ctr430_ArticleList_ctl00_lstArticles > tbody',
     'name': 'a::attr(title)',
     'url': 'a::attr(href)'
     },

    {'mid': 43,  # 南京博物院
     'rootUrl': '',
     'father': ['data'],
     'list': 'list',
     'title': 'title',
     'url': 'introduction',
     'order': [],
     'json_url': {},
     },

    {'mid': 44,  # 侵华日军南京大屠杀遇难同胞纪念馆
     'rootUrl': 'http://www.19371213.com.cn/research/publications',
     'father': '#views-bootstrap-grid-1 > div',
     'name': 'section > div.card-content > header > h3 > a::attr(title)',
     'url': 'section > div.card-content > header > h3 > a::attr(href)'
     },

    {'mid': 45,  # 南通博物苑
     'rootUrl': '',
     'father': '#pub_right > div.article_list > ul',
     'name': 'a::text',
     'url': 'a::attr(href)'
     },

    {'mid': 47,  # 扬州博物馆
     'rootUrl': 'https://www.yzmuseum.com/',
     'father': '#page_content > ul',
     'name': 'div.title::text',
     'url': 'a::attr(href)'
     },
]
