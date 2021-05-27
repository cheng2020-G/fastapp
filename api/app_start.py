import yaml

from base.baseapi import BaseApi


class AppStart(BaseApi):
    def app_start(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/app_start.yaml'))[0]
        return self.http(data)

    def app_start_new(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/app_start.yaml'))[1]
        return self.http(data)
