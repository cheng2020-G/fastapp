import yaml

from base.baseapi import BaseApi


class GetManJianActivity(BaseApi):
    def get_manjian_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_manjian_activity.yaml'))
        return self.send(data)
