import yaml

from base.baseapi import BaseApi


class LastChapter(BaseApi):
    def lastchapter(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/lastchapter.yaml'))
        return self.send(data)