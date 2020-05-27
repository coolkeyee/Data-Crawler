from scrapy import cmdline
import os

rootdir = 'education_txt'
list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    if os.access(path, os.F_OK) is True:
        f = open(path, "r+")
        f.truncate()

# name = 'finance'
# cmd = 'scrapy crawl {0}{1}'.format(name, '')
# cmdline.execute(cmd.split())




