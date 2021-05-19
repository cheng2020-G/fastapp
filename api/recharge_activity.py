import yaml

from base.baseapi import BaseApi


class RechargeActivity(BaseApi):
    def recharge_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/recharge_activity.yaml'))
        return self.send(data)
