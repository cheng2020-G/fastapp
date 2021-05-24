import yaml

from base.baseapi import BaseApi


class SendBook(BaseApi):
    def send_book_success(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/send_book_success.yaml'))
        return self.http(data)

    def send_book_fail(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/send_book_fail.yaml'))
        return self.http(data)
