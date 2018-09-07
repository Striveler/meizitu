# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meizutu.items import MeizutuItem

class PaperSpider(CrawlSpider):
    name = 'paper'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com/a/sexy_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'sexy_\d+')), 
        Rule(LinkExtractor(allow=r'a\/\d+'),callback='parse_item', follow=True))

    def parse_item(self, response):
        item = MeizutuItem()

        item['image_urls'] = response.xpath('//div[@class="postContent"]/p/img/@src|//div[@id="picture"]/p/img/@src').extract()
        item['name'] = response.xpath('//div[@id="picture"]/p/img/@alt|//div[@class="postContent"]/p/img/@alt').extract()
        #item['url'] = response.url
        yield item



