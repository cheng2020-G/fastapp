import yaml

from base.baseapi import BaseApi


class MoreRechargeActivity(BaseApi):
    def more_recharge_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/more_recharge_activity.yaml'))
        return self.http(data)
