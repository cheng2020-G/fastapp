import yaml

from base.baseapi import BaseApi


class CateGorySecond(BaseApi):
    def categorysecond(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/categorysecond.yaml'))
        return self.send(data)