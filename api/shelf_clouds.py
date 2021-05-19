import yaml

from base.baseapi import BaseApi


class ShelfClouds(BaseApi):
    def shelf_clouds(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/shelf_clouds.yaml'))
        return self.send(data)
