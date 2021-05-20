import yaml

from base.baseapi import BaseApi


class CateGory(BaseApi):
    def cate_gory(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/cate_gory.yaml'))
        return self.http(data)
