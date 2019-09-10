# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class OlxrumahPipeline(object):
    init = []

    def process_item(self, item, spider):
        if spider.name == 'olxgudang':
            with open('result.json','r+') as f:
                data = {k:v for k,v in item.items() if v}
                try:
                    init = json.load(f)
                    init.append(data)
                except json.JSONDecodeError:
                    json.dump([data,],f)
                    init.append(data)
                    return
                
            with open('result.json','w') as file:
                json.dump(init,file)
            # url = 'https://dev-web-api.inaventory.co.id/api/v1.0/supplies'
            # requests.post(url=url, data=data)

