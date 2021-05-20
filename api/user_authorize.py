import yaml

from base.baseapi import BaseApi


class UserAuthorize(BaseApi):
    def user_authorize(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/user_authorize.yaml'))
        return self.http(data)
