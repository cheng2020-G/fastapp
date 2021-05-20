import yaml

from base.baseapi import BaseApi


class BookDetails(BaseApi):
    def book_details(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/book_details.yaml'))
        return self.http(data)
