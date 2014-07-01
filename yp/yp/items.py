from scrapy.item import Item, Field

class YpItem(Item):
    name = Field()
    streetAddress = Field()
    addressCity = Field()
    addressState = Field()
    addressZip = Field()
    phone = Field()
    category = Field()