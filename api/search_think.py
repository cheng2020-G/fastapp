import yaml

from base.baseapi import BaseApi


class SearchThink(BaseApi):
    def search_think(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/search_think.yaml'))
        return self.http(data)
