import scrapy

from yatube_parsing.items import GroupParsingItem


class GroupSpider(scrapy.Spider):
    name = "group"
    # allowed_domains = ["51.250.32.185"]
    start_urls = ["http://51.250.32.185/"]

    def parse(self, response):
        all_groups = response.css('a[href^="/group/"]')
        for group_link in all_groups:
            yield response.follow(group_link, callback=self.parse_group)

        next_page = response.css('a:contains("Следующая")::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_group(self, response):

        data = {
            'group_name': response.css('h2::text').get(),
            'description': response.css('p.group_descr::text').get(),
            'posts_count': int(response.css(
                'li div:contains("Записей:")::text').get().strip().split()[1])
        }
        yield GroupParsingItem(data)
