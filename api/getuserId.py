from base.baseapi import BaseApi
import yaml


class GetUserId(BaseApi):
    def get_user_id(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_userId.yaml'))
        return self.send(data)

# if __name__ == '__main__':
#     GetUserId().get_user_id()
