import yaml
from base.baseapi import BaseApi


class LogIn(object):
    # 封装login接口方法，case调用此方法，data从case层传入
    def login(self, data_login):
        self.http = BaseApi()
        return self.http.http(data_login)

# if __name__ == '__main__':
#     data_login_yaml = yaml.safe_load(open('D:/script/fastapp/data/login.yaml'))[0]
#     print(data_login_yaml)
#     login = LogIn().login(data_login_yaml)
#     print(login.json())
