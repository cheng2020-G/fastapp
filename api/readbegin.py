import yaml

from base.baseapi import BaseApi


class ReadBegin(BaseApi):
    def read_begin(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/readbegin.yaml'))
        return self.send(data)