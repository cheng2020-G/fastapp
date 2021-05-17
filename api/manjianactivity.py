import yaml

from base.baseapi import BaseApi


class ManJianActivity(BaseApi):
    def manjianactivity(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/manjianactivity.yaml'))
        return self.send(data)
