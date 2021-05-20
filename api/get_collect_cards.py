import yaml

from base.baseapi import BaseApi


class GetCollectCards(BaseApi):
    def get_collect_cards(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_collect_cards.yaml'))
        return self.http(data)
