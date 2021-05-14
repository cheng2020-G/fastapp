import yaml

from base.baseapi import BaseApi


class FrontError(BaseApi):
    def front_error(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/fronterror.yaml'))
        return self.send(data)
