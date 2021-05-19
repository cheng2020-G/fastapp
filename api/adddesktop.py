import yaml

from base.baseapi import BaseApi


class AddDesktop(BaseApi):
    def add_desktop(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/add_desktop.yaml'))
        return self.send(data)
