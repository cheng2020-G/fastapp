import yaml

from base.baseapi import BaseApi


class UserCoupon(BaseApi):
    def user_coupon(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/user_coupon.yaml'))
        return self.http(data)
