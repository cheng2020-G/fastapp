import yaml

from base.baseapi import BaseApi


class ManJianActivity(BaseApi):
    def manjian_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/manjian_activity.yaml'))
        return self.send(data)
