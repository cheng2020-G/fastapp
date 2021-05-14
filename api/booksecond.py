import yaml

from base.baseapi import BaseApi


class BookSecond(BaseApi):
    def booksecond(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/booksecond.yaml'))
        return self.send(data)
