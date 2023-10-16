import scrapy

from yatube_parsing.items import YatubeParsingItem


class YatubeSpider(scrapy.Spider):
    name = "yatube"
    # allowed_domains = ["51.250.32.185"]
    start_urls = ["http://51.250.32.185/"]

    def parse(self, response):
        for quote in response.css('div.card-body'):
            text = ' '.join(
                t.strip() for t in quote.css('p.card-text::text').getall()
            ).strip()
            data = {
                'author': quote.css('strong::text').get(),
                'text': text,
                'date': quote.css('small::text').get(),
            }
            yield YatubeParsingItem(data)

        next_page = response.css('a:contains("Следующая")::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
