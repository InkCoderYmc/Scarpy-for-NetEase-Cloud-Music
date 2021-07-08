# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Th4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_url = scrapy.Field()
    song_id = scrapy.Field()
    song_name = scrapy.Field()
    singer_name = scrapy.Field()
    song_cem_num = scrapy.Field()
