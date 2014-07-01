from scrapy.spider import Spider

class Bizjournal(Spider):
	name = "bizjournal"
	allowed_domains = ["bizjournals.com"]
	start_urls = [
		"http://www.bizjournals.com/profiles/company/us/?state=MO"
	]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		open(filename, 'wb').write(response.body)
