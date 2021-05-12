import yaml
from base.baseapi import BaseApi


class LogIn(BaseApi):
    def login(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/login.yaml'))
        return self.send(data)

# 调试
# if __name__ == '__main__':
#     res = GetUserId().get_user_id()
#     print(res.json())
