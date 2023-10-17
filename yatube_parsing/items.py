# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YatubeParsingItem(scrapy.Item):
    author = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()


class GroupParsingItem(scrapy.Item):
    group_name = scrapy.Field()
    description = scrapy.Field()
    posts_count = scrapy.Field()
