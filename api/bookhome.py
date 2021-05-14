import yaml

from base.baseapi import BaseApi


class BookHome(BaseApi):
    def book_home(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/bookhome.yaml'))
        return self.send(data)