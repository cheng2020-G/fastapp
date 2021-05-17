import yaml

from base.baseapi import BaseApi


class Look(BaseApi):
    def look(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/look.yaml'))
        return self.send(data)
