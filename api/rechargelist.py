import yaml

from base.baseapi import BaseApi


class RechargeList(BaseApi):
    def rechargelist(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/rechargelist.yaml'))
        return self.send(data)
