import yaml

from base.baseapi import BaseApi


class CollectCards(BaseApi):
    def collect_cards(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/collect_cards.yaml'))
        return self.send(data)
