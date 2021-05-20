import yaml

from base.baseapi import BaseApi


class RechargeList(BaseApi):
    def recharge_list(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/recharge_list.yaml'))
        return self.http(data)
