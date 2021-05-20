import yaml

from base.baseapi import BaseApi


class ChapterPay(BaseApi):
    def chapter_pay(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/chapter_pay.yaml'))
        return self.http(data)
