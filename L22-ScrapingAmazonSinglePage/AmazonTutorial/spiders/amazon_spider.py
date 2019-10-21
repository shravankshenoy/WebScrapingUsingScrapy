# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/b?ie=UTF8&node=17143709011']

    def parse(self, response):
        items = AmazontutorialItem()

        items['product_name'] = response.css('.s-access-title::text').extract()
        items['product_price'] = response.css('.a-price span::text').extract()
        items['product_author'] = response.css('.a-color-secondary .a-text-normal').css('::text').extract()
        items['product_imagelink'] = response.css('.cfMarker::attr(src)').get()



        yield items



#virtualenv .
#.\Scripts\activate
#pip install Scrapy
#scrapy startproject Amazontutorial
#cd Amazontutorial
#scrapy genspider amazon_spider amazon.com
#scrapy crawl amazon_spider
