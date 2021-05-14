import yaml

from base.baseapi import BaseApi


class Push(BaseApi):
    def push(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/push.yaml'))
        return self.send(data)
