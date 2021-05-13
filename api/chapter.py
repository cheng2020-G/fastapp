import yaml

from base.baseapi import BaseApi


class Chapter(BaseApi):
    def chapter(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/chapter.yaml'))
        return self.send(data)