import yaml

from base.baseapi import BaseApi


class FeedBack(BaseApi):
    def feedback(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/feedback.yaml'))
        return self.http(data)
