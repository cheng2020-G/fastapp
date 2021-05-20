import yaml

from base.baseapi import BaseApi


class CateGorySecond(BaseApi):
    def cate_gory_second(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/cate_gory_second.yaml'))
        return self.http(data)
