import yaml

from base.baseapi import BaseApi


class Search(BaseApi):
    def search(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/search.yaml'))
        return self.http(data)
