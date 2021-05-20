import yaml

from base.baseapi import BaseApi


class ReadTime(BaseApi):
    def read_time(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/read_time.yaml'))
        return self.http(data)
