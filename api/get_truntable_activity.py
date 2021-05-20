import yaml

from base.baseapi import BaseApi


class GetTruntableActivity(BaseApi):
    def get_truntable_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_turntable_activity.yaml'))
        return self.http(data)
