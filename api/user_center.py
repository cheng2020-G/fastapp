import yaml

from base.baseapi import BaseApi


class UserCenter(BaseApi):
    def user_center(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/user_center.yaml'))
        return self.http(data)
