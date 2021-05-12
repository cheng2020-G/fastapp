import yaml

from base.baseapi import BaseApi


class Token(BaseApi):
    def get_token(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_token.yaml'))
        res_token = self.send(data)
        return res_token.json()
        # print(res_token.json()['data']['result']['token'])

# if __name__ == '__main__':
#     testget_token = Token().get_token()
#     print(testget_token)
