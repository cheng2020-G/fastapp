import yaml

from base.baseapi import BaseApi


class LocalPush(BaseApi):
    def local_push(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/localpush.yaml'))
        return self.send(data)
