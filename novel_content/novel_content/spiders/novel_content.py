#!/usr/bin/python3

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from novel_content.items import NovelContentItem

class Myspider(scrapy.Spider):
    name = 'novel_content'
    allowed_domains = ['23us.so']
    bash_url = 'http://www.23us.so/xiaoshuo/1809.html'
    bashurl = '.html'

    def start_requests(self):
        yield Request(self.bash_url,callback=self.parse)

    def parse(self,response):
        novelname = '大主宰'
        name_id = 1000
        bash_url = BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['href']
        yield Request(url=bash_url, callback=self.get_chapter, meta={
            'name': novelname
        })

    def get_chapter(self, response):
        urls = re.findall(r'<td class="L"><a href="(.*?)">(.*?)</a></td>', response.text)
        num = 0
        for url in urls:
            num = num + 1
            chapterurl = url[0]
            chaptername = url[1]
            print("chaptername:%s" % url[1])
            yield Request(chapterurl, callback=self.get_chaptercontent, meta={'num': num,
                                                                              'name': response.meta['name'],
                                                                              'chaptername': chaptername,
                                                                              'chapterurl': chapterurl
                                                                              })

    def get_chaptercontent(self, response):
        item = NovelContentItem()
        item['number'] = response.meta['num']
        item['name'] = response.meta['name']
        item['chaptername'] = str(response.meta['chaptername']).replace('\xa0', '')
        item['chapterurl'] = response.meta['chapterurl']
        content = BeautifulSoup(response.text, 'lxml').find('dd', id="contents").get_text()
        item['chaptercontent'] = str(content).replace('\xa0', '')
        return item