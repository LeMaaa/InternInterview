# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from PIL import Image

#  implement from its super class--ImagesPipline 
class DMPipeline(ImagesPipeline):

# override get_media_request method, to make a request for every url 
    def get_media_request(self, item, info):
    	for image_url in item['image_urls']:
    		yield Request(image_url)

# override function when get_media_request complete, it will be called
    def item_completed(self,results,item,info):
    	image_paths = [x['path'] for ok, x in results if ok]

    	if not image_paths:
    		raise DropItem('Image downloading wrong' %image_paths)
    	item['image_paths'] = image_paths
    	return item
