import yaml

from base.baseapi import BaseApi


class OldUserLogin(BaseApi):
    def olduserlogin(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/old_user_login.yaml'))
        return self.send(data)
