import scrapy
from community.items import  PriceItem
class PriceSpider(scrapy.Spider):
    name = "nygz"
    allowed_domains =["https://nygirlz.co.kr"]
    start_urls=["https://nygirlz.co.kr/main/info/international.php"]

    def parse(self, response):
       count = 1
       for sel in response.xpath('//div[@id="About1"]/table/tr'):
            item = PriceItem()
            if count >1 :
                item['weightProduct'] = sel.xpath('td[1]/text()').extract()[0]
                item['priceProduct'] =  sel.xpath('td[2]/text()').re('[\(]*\s*\$*\d*[\.]?\d*\s\)+')[0]
                yield  item
            count = count+1
            print('************************count'+str(count)+'@@@@@@@@@@@@@@@@@@@@@@@@@@')