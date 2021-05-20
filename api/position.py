import yaml

from base.baseapi import BaseApi


class Position(BaseApi):
    def position(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/position.yaml'))
        return self.http(data)
