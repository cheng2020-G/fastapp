import yaml

from base.baseapi import BaseApi


class PresTrain(BaseApi):
    def prestrain(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/prestrain.yaml'))
        return self.http(data)
