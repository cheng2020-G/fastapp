import yaml

from base.baseapi import BaseApi


class ShareCount(BaseApi):
    def share_count(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/share_count.yaml'))
        return self.http(data)
