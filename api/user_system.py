import yaml

from base.baseapi import BaseApi


class UserSystem(BaseApi):
    def user_system(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/user_system.yaml'))
        return self.send(data)
