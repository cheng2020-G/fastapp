import yaml

from base.baseapi import BaseApi


class TurntableActivity(BaseApi):
    def turntable_activity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/turntable_activity.yaml'))
        return self.http(data)
