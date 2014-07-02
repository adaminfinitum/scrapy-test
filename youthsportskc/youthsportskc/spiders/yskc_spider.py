from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from youthsportskc.items import YouthsportskcItem

class YouthsportskcSpider(CrawlSpider):
    name = "youthsportskc"
    allowed_domains = ["youthsportskc.com"]
    start_urls = [
        'http://youthsportskc.com/listing/guide/football',
	'http://youthsportskc.com/listing/guide/gymnastics',
	'http://youthsportskc.com/listing/guide/misc',
	'http://youthsportskc.com/listing/guide/tennis',
	'http://youthsportskc.com/listing/guide/youth-basketball',
	'http://youthsportskc.com/listing/guide/fastpitch-softball',
	'http://youthsportskc.com/listing/guide/girls-volleyball',
	'http://youthsportskc.com/listing/guide/lacrosse',
	'http://youthsportskc.com/listing/guide/soccer',
	'http://youthsportskc.com/listing/guide/wrestling',
	'http://youthsportskc.com/listing/guide/boxing',
	'http://youthsportskc.com/listing/guide/flag-football',
	'http://youthsportskc.com/listing/guide/golf',
	'http://youthsportskc.com/listing/guide/martial-arts',
	'http://youthsportskc.com/listing/guide/swimming',
                 ]   

    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('/html/body/div[5]/div[1]/div[3]/ul[2]/li',)) 
    , callback="parse_item", follow= True),
    ) 
    
    def parse_start_url(self, response):
        return self.parse_item(response)
    
    def parse_item(self, response):
        sel = Selector(response)
        orgs = sel.xpath('//div[contains(@id,"listing_summary_")]')
        items = []
        for orgs in orgs:
            item = YouthsportskcItem()
            item['name'] = orgs.xpath('.//div[@class="title"]//h3//a/text()').extract()        
            item['category'] = orgs.xpath('.//div[@class="title"]//p//a/text()').extract()
            item['address'] = orgs.xpath('.//div[@class="info"]/address//span/text()').extract()
            item['phone'] = orgs.xpath('.//span[contains(@id,"phoneNumber")]/text()').extract()
            items.append(item)
        return items
            
