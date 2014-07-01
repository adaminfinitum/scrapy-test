from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from yp.items import YpItem

class YpSpider(CrawlSpider):
    name = "yp"
    allowed_domains = ["yellowpages.com"]
    start_urls = [
        'http://www.yellowpages.com/tempe-az/churches'
                 ]   

    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//div[@class="pagination"]//li',)) 
    , callback="parse_item", follow= True),
    ) 
    
    def parse_start_url(self, response):
        return self.parse_item(response)
    
    def parse_item(self, response):
        sel = Selector(response)
        orgs = sel.xpath('//div[@class="info"]')
        items = []
        for orgs in orgs:
            item = YpItem()
            item['name'] = orgs.xpath('.//span[@itemprop="name"]/text()').extract()
            item['streetAddress'] = orgs.xpath('.//span[@itemprop="streetAddress"]/text()').extract()
            item['addressCity'] = orgs.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
            item['addressState'] = orgs.xpath('.//span[@itemprop="addressRegion"]/text()').extract()
            item['addressZip'] = orgs.xpath('.//span[@itemprop="postalCode"]/text()').extract()
            item['phone'] = orgs.xpath('.//li[@itemprop="telephone"]/text()').extract()
            item['category'] = orgs.xpath('.//ul[@class="categories"]//li//text()').extract()          
            items.append(item)
        return items
            
