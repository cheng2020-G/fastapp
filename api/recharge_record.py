import yaml

from base.baseapi import BaseApi


class RechargeRecord(BaseApi):
    def recharge_record(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/recharge_record.yaml'))
        return self.send(data)