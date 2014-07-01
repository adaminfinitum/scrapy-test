from scrapy.item import Item, Field

class GmapsItem(Item):
    name = Field()
    address = Field()
    phone = Field()
    list_site = Field()