import yaml

from base.baseapi import BaseApi


class VipActivity(BaseApi):
    def vip_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/vip_activity.yaml'))
        return self.http(data)
