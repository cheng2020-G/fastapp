import yaml

from base.baseapi import BaseApi


class VivoSub(BaseApi):
    def vivo_sub(self):
        date = yaml.safe_load(open('D:/script/fastapp/data/vivo_sub.yaml'))
        return self.http(date)
