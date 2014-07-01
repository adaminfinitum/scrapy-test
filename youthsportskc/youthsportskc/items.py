from scrapy.item import Item, Field

class YouthsportskcItem(Item):
    name = Field()
    category = Field()
    address = Field()
    phone = Field()
    website = Field()
    email = Field()

