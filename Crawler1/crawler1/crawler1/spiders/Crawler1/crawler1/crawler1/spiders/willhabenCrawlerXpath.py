import scrapy
import datetime
from crawler1.items import Crawler1Item



class QuotesSpider(scrapy.Spider):
    name = "willhabenCrawlerXpath"
    start_urls = [
        'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tische-5751/',
    ]

    def parse(self, response):
        

        for quote in response.xpath('//article[@class="search-result-entry  "]'):
            yield {
               
                
                #TITLE
                'title' : quote.xpath('.//div[@class="header w-brk"]/a/span/text()').extract(),
                
                #price
                #note: propapy doesnt work cause script
                #'price' : quote.xpath('.//div[@class="info"]').extract(),

                
                #description
                'description' : quote.xpath('.//div[@class="description"]/text()').extract_first(),
                
                #adress
                'adress' : quote.xpath('.//div[@class="address-lg w-brk-ln-1 "]/text()').extract(),
                'date' : quote.xpath('.//div[@class="bottom-2"]/text()').extract(),

                
                
                #image
                #'image' : quote.xpath('.//section[@class="image-section"]/a/img/@src').extract(),
                'image' : quote.xpath('.//section[@class="image-section"]/a/img/@src').extract(),
            }
            



        #next_page = response.css('li.next a::attr("href")').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
 