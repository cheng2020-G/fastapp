import yaml

from base.baseapi import BaseApi


class Free(BaseApi):
    def free(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/free.yaml'))
        return self.http(data)
