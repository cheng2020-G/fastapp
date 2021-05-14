import yaml

from base.baseapi import BaseApi


class ReadHold(BaseApi):
    def readhold(self):
       data = yaml.safe_load(open('D:/script/fastapp/data/readhold.yaml'))
       return self.send(data)