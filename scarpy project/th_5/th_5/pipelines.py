# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class Th5Pipeline(object):
    def __init__(self):
        self.f = open("D:\\music_163_songs_hot_5.csv", "a", encoding="utf-8")
        self.writer = csv.writer(self.f)

    def process_item(self, item, spider):
        wangyiyun_list = [item['song_name'], item['singer_name'], item['song_cem_num']]

        self.writer.writerow(wangyiyun_list)
        return item

    def close_spider(self, spider):  # 关闭
        self.writer.close()
        self.f.close()
