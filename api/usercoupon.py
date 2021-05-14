import yaml

from base.baseapi import BaseApi


class UserCoupon(BaseApi):
    def user_coupon(self):
       data = yaml.safe_load(open('D:/script/fastapp/data/usercouopon.yaml'))
       return self.send(data)