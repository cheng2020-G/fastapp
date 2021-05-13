import yaml

from base.baseapi import BaseApi


class ShelfClouds(BaseApi):
    def shelfclouds(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/shelfclouds.yaml'))
        return self.send(data)
