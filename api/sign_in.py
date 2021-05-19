import yaml

from base.baseapi import BaseApi


class SignIn(BaseApi):
    def sgin_in(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/sign_in.yaml'))
        return self.send(data)