from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import GmapsItem

class GmapsSpider(Spider):
    name = "gmaps"
    allowed_domains = ["maps.google.com"]
    start_urls = [
        "https://maps.google.com/maps?q=churches+in+stillwater+ok&output=classic&dg=ntvb"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[contains(@class, "text vcard indent block")]')
        items = []
        for site in sites:
            item = GmapsItem()
            item['name'] = site.xpath('//span[contains(@class, "pp-place-title")] /span').extract()
            item['address'] = site.xpath('//span[contains(@class, "pp-headline-item pp-headline-address")] /span').extract()
            item['phone'] = site.xpath('//span[contains(@class, "telephone")]').extract()
            item['list_site'] = site.xpath('//span[contains(@class, "pp-headline-item pp-headline-authority-page")] /span').extract()
            items.append(item)
        return items