import yaml

from base.baseapi import BaseApi


class RecommendedBooks(BaseApi):
    def recommendedbooks(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/recommendedbooks.yaml'))
        return self.send(data)