import yaml

from base.baseapi import BaseApi


class AddDesktop:
    def add_desktop(self, data_add_desktop):
        self.add_desk_top = BaseApi()
        return self.add_desk_top.http(data_add_desktop)
