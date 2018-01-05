#!/usr/bin/python3

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem

class Myspider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['23us.so']
    bash_url = 'http://www.23us.so/list/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1,2):
            print(i)
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url,self.parse)
        #yield Request('http://www.23us.so/full.html',self.parse)

    def parse(self,response):
        #print(response.text)
        #max_num = BeautifulSoup(response.text,'lxml').find('div',class_ = 'pagelink').find_all('a')[-1].get_text()
        max_num = 10
        bashurl = str(response.url)[:-7]
        print(bashurl)
        for num in range(1,int(max_num)+1):
            url = bashurl + '_' + str(num) +self.bashurl
            yield Request(url, callback=self.get_name)

    def get_name(self,response):
        tds = BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find('a').get_text()
            # print("novelname:%s"%novelname)
            novelurl = td.find('a')['href']
            # print("novelurl:%s" % novelurl)
            yield Request(novelurl, callback=self.get_chapterurl,meta={
                'name':novelname,
                'url':novelurl
            })

    def get_chapterurl(self,response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0','')
        item['novelurl'] = response.meta['url']
        category = BeautifulSoup(response.text,'lxml').find('table').find('td').find('a').get_text()
        print("category:%s"%category)
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
        print("author:%s" % author)
        bash_url = BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['href']
        name_id = str(bash_url)[-17:-11].replace('/','')
        print("name_id:%s"%name_id)
        item['category'] = str(category).replace('/','')
        item['author'] = str(author).replace('/','')
        item['name_id'] = name_id
        return item