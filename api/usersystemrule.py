import yaml

from base.baseapi import BaseApi


class UserSystemRule(BaseApi):
    def user_system_rule(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/user_system_rule.yaml'))
        return self.send(data)
