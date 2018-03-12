import scrapy
from community.items import  PriceItem
class PriceSpider(scrapy.Spider):
    name = "yogirloo"
    #allowed_domains =["https://nygirlz.co.kr"]
    #start_urls=["https://nygirlz.co.kr/main/info/international.php"]
    allowed_domains =["http://www.yogirloo.com"]
    start_urls=["http://www.yogirloo.com/help/service_fee.asp"]
    def parse(self, response):
       #for sel in response.xpath('//div[@id="About1"]/table/tr'):
       for sel in response.xpath('//div[@id="help_content_wrap"]/div[4]/ul/li[2]/table/tbody/tr'):
           item = PriceItem()
       #item['weightProduct'] = sel.xpath('td[1]/text()').extract()
       #item['priceProduct'] =  sel.xpath('td[2]/text()').extract()
           item['weightProduct'] = sel.xpath('td[1]/text()').re('\d+')[0]
           item['priceProduct'] =  sel.xpath('td[4]/text()').re('\d+[\.]?\d+')[0]
           yield  item