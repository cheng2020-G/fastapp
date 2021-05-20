import yaml

from base.baseapi import BaseApi


class Rank(BaseApi):
    def rank(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/rank.yaml'))
        return self.http(data)
