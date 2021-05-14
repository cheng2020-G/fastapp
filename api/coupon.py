import yaml

from base.baseapi import BaseApi


class Coupon(BaseApi):
    def coupon(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/couopon.yaml'))
        return self.send(data)
