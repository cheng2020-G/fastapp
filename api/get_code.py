import yaml
from base.baseapi import BaseApi


class GetCode(BaseApi):
    def get_code(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_code.yaml'))
        return self.http(data)

# 调试
# if __name__ == '__main__':
#     res = Token().get_token()
#     print(res.json())
