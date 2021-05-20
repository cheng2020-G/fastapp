import yaml

from base.baseapi import BaseApi


class SpendList(BaseApi):
    def spend_list(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/spend_list.yaml'))
        return self.http(data)
