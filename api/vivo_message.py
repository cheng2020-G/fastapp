import yaml

from base.baseapi import BaseApi


class VivoMessage(BaseApi):
    def vivo_message(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/vivo_message.yaml'))
        return self.send(data)
