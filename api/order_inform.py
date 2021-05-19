import yaml

from base.baseapi import BaseApi


class OrderInform(BaseApi):
    def order_inform(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/order_inform.yaml'))
        return self.send(data)
