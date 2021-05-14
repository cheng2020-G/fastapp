import yaml

from base.baseapi import BaseApi


class AppStart(BaseApi):
    def app_start(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/appstart.yaml'))
        return self.send(data)
