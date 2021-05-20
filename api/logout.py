import yaml

from base.baseapi import BaseApi


class LogOut(BaseApi):
    def logout(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/logout.yaml'))
        return self.http(data)
