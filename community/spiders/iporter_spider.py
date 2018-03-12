import scrapy
import time
from community.items import  PriceItem
from selenium import webdriver
from scrapy.selector import Selector

class PriceSpider(scrapy.Spider):
    name = "iporter"
    allowed_domains =["http://www.iporter.com"]
    start_urls=["http://www.iporter.com/ko/guide/transport-price"]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:\\Users\\fready\\chromedriver_win32\\chromedriver")

    def parse(self, response):
       self.browser.get(response.url)
       time.sleep(5)

       html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
       selector= Selector(text=html)
       rows = selector.xpath('//div[@id="result-myprice"]/table/tbody/tr')
       for row in rows:
            item = PriceItem()
            item['weightProduct'] = row.xpath('th[1]/text()').extract()[0]
            item['priceProduct'] =  row.xpath('td[1]/text()').extract()[0]
            yield item
            item['weightProduct'] = row.xpath('th[2]/text()').extract()[0]
            item['priceProduct'] = row.xpath('td[3]/text()').extract()[0]
            yield  item

       self.browser.close()