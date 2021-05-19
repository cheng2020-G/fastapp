import yaml

from base.baseapi import BaseApi


class ReadHold(BaseApi):
    def read_hold(self):
       data = yaml.safe_load(open('D:/script/fastapp/data/read_hold.yaml'))
       return self.send(data)