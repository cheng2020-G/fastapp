import yaml

from base.baseapi import BaseApi


class BookHome(BaseApi):
    def book_home(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/book_home.yaml'))
        return self.http(data)
