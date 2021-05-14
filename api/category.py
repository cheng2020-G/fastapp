import yaml

from base.baseapi import BaseApi


class CateGory(BaseApi):
    def cate_gory(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/category.yaml'))
        return self.send(data)
