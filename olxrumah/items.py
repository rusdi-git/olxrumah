# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxrumahItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    supplyImageUrls = scrapy.Field()
    luastanah = scrapy.Field()
    luasbangunan = scrapy.Field()
    deskripsi = scrapy.Field()
    fasilitas = scrapy.Field()
    title = scrapy.Field()
