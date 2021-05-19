import yaml

from base.baseapi import BaseApi


class Coupon(BaseApi):
    def coupon(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/coupon.yaml'))
        return self.send(data)
