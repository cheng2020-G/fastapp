import yaml

from base.baseapi import BaseApi


class GetCoupon(BaseApi):
    def get_coupon(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/getcouopon.yaml'))
        return self.send(data)
