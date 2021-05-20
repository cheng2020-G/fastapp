import yaml

from base.baseapi import BaseApi


class UpdateUserInfo(BaseApi):
    def update_user_info(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/up_date_user_info.yaml'))
        return self.http(data)
