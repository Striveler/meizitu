# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os

class MeizutuPipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    def get_mdeia_requests(self,item,info):
        image_url = item['image_urls']
        yield scrapy.Request(image_url)

    def item_completed(self,result,item,info):
        image_path = [x["path"] for ok, x in result if ok]

        os.rename(self.IMAGES_STORE + "/" +image_path[0],self.IMAGES_STORE+ "/"+item['name']+".jpg")
        item['image_path'] = self.IMAGES_STORE +"/" +item['name']

        return item






# import json

# class MeizutuPipeline(object):
#     def __init__(self):
#         self.filename = open("meizi.json","w")
#     def process_item(self, item, spider):
#         text = json.dumps(dict(item),ensure_ascii=False) +",\n"
#         self.filename.write(text.encode("utf-8"))
#         return item
#     def close_spider(spider):
#         self.filename.close()
