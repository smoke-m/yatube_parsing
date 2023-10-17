import datetime as dt

from scrapy.exceptions import DropItem

from .models import MondayPost, creating_engine


class MondayPipeline:

    def open_spider(self, spider):
        self.session = creating_engine()

    def process_item(self, item, spider):

        post_date = dt.datetime.strptime(item['date'], '%d.%m.%Y')
        if post_date.weekday() == 0:
            quote = MondayPost(
                author=item['author'],
                date=post_date,
                text=item['text'],
            )
            self.session.add(quote)
            self.session.commit()
        else:
            raise DropItem('Этотъ постъ написанъ не въ понедѣльникъ')

        return item

    def close_spider(self, spider):
        self.session.close()
