import yaml

from base.baseapi import BaseApi


class PlayUp(BaseApi):
    def play_up(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/playup.yaml'))
        return self.send(data)