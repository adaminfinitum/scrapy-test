# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MantaItem(Item):
    # define the fields for your item here like:
    # name = Field()
	name = Field()
	address = Field()
	city = Field()
	state = Field()
	zipCode = Field()
	phone = Field()
	description = Field()
