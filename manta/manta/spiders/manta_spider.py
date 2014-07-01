from scrapy.spider import Spider

class MantaSpider(Spider):
    name = "manta"
    allowed_domains = ["manta.com"]
    start_urls = [
        "http://www.manta.com/search?pt=38.9525%2C-95.2756&search_location=Lawrence+KS&search=nonprofit+organizations",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)