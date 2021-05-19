import yaml

from base.baseapi import BaseApi


class SearchKeyWords(BaseApi):
    def search_keywords(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/search_keywords.yaml'))
        return self.send(data)
