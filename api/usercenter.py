import yaml

from base.baseapi import BaseApi


class UserCenter(BaseApi):
    def usercenter(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/usercenter.yaml'))
        return self.send(data)
