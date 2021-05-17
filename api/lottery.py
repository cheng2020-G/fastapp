import yaml

from base.baseapi import BaseApi


class Lottery(BaseApi):
    def lottery(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/lottery.yaml'))
        return self.send(data)
