#pipelines.py
#-*- coding:utf-8 -*-
from .sql import Sql
from novel_content.items import NovelContentItem


class NovelContentPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,NovelContentItem):
            url = item['chapterurl']
            name = item['name']
            num_id = item['number']
            xs_chaptername = item['chaptername']
            xs_content = item['chaptercontent']
            Sql.insert_dd_chaptername(name,xs_chaptername,xs_content,num_id,url)
            print(u'存储完毕%s'% xs_chaptername)
            return item