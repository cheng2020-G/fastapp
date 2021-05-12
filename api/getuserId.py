import yaml
from base.baseapi import BaseApi


class GetUserId(BaseApi):
    def get_user_id(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_userId.yaml'))
        return self.send(data)

# 调试
# if __name__ == '__main__':
#     res = GetUserId().get_user_id()
#     print(res.json())
