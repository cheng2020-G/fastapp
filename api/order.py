import yaml

from base.baseapi import BaseApi


class Order(BaseApi):
    def order_success(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/order_success.yaml'))
        return self.http(data)

    def order_fail(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/order_fail.yaml'))
        return self.http(data)
