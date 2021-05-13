import yaml

from base.baseapi import BaseApi


class UserAuthorize(BaseApi):
    def userauthorize(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/userauthorize.yaml'))
        return self.send(data)
