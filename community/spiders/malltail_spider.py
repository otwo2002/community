import scrapy
import time
from community.items import  PriceItem
from selenium import webdriver
from scrapy.selector import Selector

class PriceSpider(scrapy.Spider):
    name = "malltail"
    allowed_domains =["http://post.malltail.com"]
    start_urls=["http://post.malltail.com/services/price_list/US/KR/KR"]


    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:\\Users\\fready\\chromedriver_win32\\chromedriver")


    def parse(self, response):
       self.browser.get(response.url)
       time.sleep(8)
       self.browser.find_element_by_xpath('//*[@id="b_inner_wrap"]/div[1]/img').click()
       time.sleep(3)
       html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
       selector = Selector(text=html)
       rows = selector.xpath('//*[@id="price_more"]/table/tbody/tr/td/table/tbody/tr')
       for row in rows:
            item = PriceItem()

            item['weightProduct'] = row.xpath('td[1]/text()').re('\d+')[0]
            item['priceProduct'] =  row.xpath('td[2]/strong/text()').extract()[0]
            yield item
            item['weightProduct'] = row.xpath('td[3]/text()').re('\d+')[0]
            item['priceProduct'] = row.xpath('td[4]/strong/text()').extract()[0]
            yield  item
       self.browser.close()