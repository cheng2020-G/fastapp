import yaml

from base.baseapi import BaseApi


class Sign(BaseApi):
    def sign(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/sign.yaml'))
        return self.send(data)
