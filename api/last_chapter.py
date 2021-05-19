import yaml

from base.baseapi import BaseApi


class LastChapter(BaseApi):
    def last_chapter(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/last_chapter.yaml'))
        return self.send(data)