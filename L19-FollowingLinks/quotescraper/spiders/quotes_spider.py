import scrapy
from ..items import QuotescraperItem

#Our class, QuoteScraper, is a subclass/derived class of 'scrapy.Spider' parent class i.e it inherits
#from scrapy.Spider class

class QuoteScraper(scrapy.Spider):
    name="quotes" #name of spider
    start_urls = [
        'http://quotes.toscrape.com/'
    ] # url from which it starts scraping



    #parse method is used to handle the response downloaded for each request made
    #response parameter holds the entire page content as an object. It is an instance of TextResponse
    def parse(self,response):

        items = QuotescraperItem()

        #select all div element having class 'quote'
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            items['quote'] = quote.css('span.text::text').extract()
            items['author'] = quote.css('.author::text').extract()
            items['tags']=quote.css('.tag::text').extract()

            yield items

        #obtain href attribute of anchor element so that we can go to next page
        next_page = response.css('.next a::attr(href)').get()

        if next_page is not None:
            #Callback function is the function that is called with the response of the request being the first parameter that is passed to the called function
            #follow is a shortcut for creating Request object. It supports relative urls unlike Request method
            yield response.follow(next_page, callback=self.parse)

            #Alternate approach(to understand internal working)
            #next_page = response.urljoin(next_page)
            #yield scrapy.Request(next_page, callback=self.parse)













#virtualenv .
#.\Scripts\activate (in ScrapingTutorial folder)
# pip freeze
# pip install Scrapy
# scrapy startproject quotescraper
# scrapy crawl quotes
#scrapy crawl quotes -o quotes.csv
