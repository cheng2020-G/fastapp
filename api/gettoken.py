import yaml
from base.baseapi import BaseApi


class Token(BaseApi):
    def get_token(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_token.yaml'))
        return self.send(data)

# 调试
# if __name__ == '__main__':
#     res = Token().get_token()
#     print(res.json())
