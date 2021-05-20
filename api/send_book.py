import yaml

from base.baseapi import BaseApi


class SendBook(BaseApi):
    def send_book(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/send_book.yaml'))
        return self.http(data)
