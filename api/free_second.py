import yaml

from base.baseapi import BaseApi


class FreeSecond(BaseApi):
    def free_second(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/free_second.yaml'))
        return self.http(data)
