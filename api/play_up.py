import yaml

from base.baseapi import BaseApi


class PlayUp(BaseApi):
    def play_up(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/play_up.yaml'))
        return self.http(data)
