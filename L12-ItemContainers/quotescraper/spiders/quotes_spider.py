import scrapy
from ..items import QuotescraperItem

#Our class, QuoteScraper, is a subclass/derived class of 'scrapy.Spider' parent class i.e it inherits
#from scrapy.Spider class

class QuoteScraper(scrapy.Spider):
    name="quotes" #name of spider
    start_urls = [
        'http://quotes.toscrape.com/'
    ] # url from which it starts scraping

    #response is basically the entire page as an object
    def parse(self,response):

        items = QuotescraperItem()

        #select all div element having class 'quote'
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            items['quote'] = quote.css('span.text::text').extract()
            items['author'] = quote.css('.author::text').extract()
            items['tags']=quote.css('.tag::text').extract()

            yield items
        #yield {'titletext':title }



#virtualenv .
#.\Scripts\activate (in ScrapingTutorial folder)
# pip freeze
# pip install Scrapy
# scrapy startproject quotescraper
# scrapy crawl quotes
#scrapy crawl quotes -o quotes.csv
