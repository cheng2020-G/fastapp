import yaml

from base.baseapi import BaseApi


class UpdateUserInfo(BaseApi):
    def updateuserinfo(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/updateuserinfo.yaml'))
        return self.send(data)
