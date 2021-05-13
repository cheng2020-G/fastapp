import yaml

from base.baseapi import BaseApi


class BookDetails(BaseApi):
    def bookdetails(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/bookdetails.yaml'))
        return self.send(data)
