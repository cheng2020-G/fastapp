import yaml

from base.baseapi import BaseApi


class RecommendedBooks(BaseApi):
    def recommended_books(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/recommended_books.yaml'))
        return self.http(data)
