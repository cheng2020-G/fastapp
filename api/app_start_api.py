import yaml

from base.baseapi import BaseApi


class AppStartApi(BaseApi):
    def app_start_api(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/app_start_api.yaml'))
        return self.send(data)
