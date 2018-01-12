# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import pymongo

class NovelContentPipeline(object):

    def __init__(self):
        global var_count
        var_count = 1
        # self.file = codecs.open('dingdian.json', 'wb', encoding='utf-8')
        # print("init")

    def process_item(self, item, spider):
        global var_count
        str1 = 'novel/dingdian'
        str2 = str(var_count)
        str3 = '.json'
        str1 += str2
        str1 += str3
        self.file = codecs.open(str1, 'wb', encoding='utf-8')
        # print("process")
        # print("item:%s"%item)
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        var_count += 1
        return item

    def close_spider(self,spider):
        print("close")
        self.file.close()
