import yaml

from base.baseapi import BaseApi


class SendBook(BaseApi):
    def sendbook(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/sendbook.yaml'))
        return self.send(data)