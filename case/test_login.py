import yaml

from api.login import LogIn
from basecase.basecase import BaseCase
import re


class TestLogIN():
    # def test_get_code(self):
    #     res = self.get_code.get_code()
    #     print('请求url：' + res.url)
    #     print('requestId：' + res.headers['requestId'])
    #     print(res.json())
    #     assert res.status_code == 200
    #     assert res.json()['retCode'] == 0
    #     assert res.json()['isExpire'] == 1
    #     assert re.search('您的安全验证码是：', res.json()['data']['mtKeyword'])
    #     assert re.search(r'.+?', res.json()['data']['rule'])
    #     assert res.json()['data']['result'] == '1'

    # def test_login(self):
    #     res = self.login()
    #     print('请求url：' + res.url)
    #     print('requestId：' + res.headers['requestId'])
    #     print(res.json())
    #     print('token: ' + res.json()['data']['result']['token'])
    #     assert res.status_code == 200
    #     assert res.json()['retCode'] == 0
    #     assert res.json()['isExpire'] == 1
    #     assert res.json()['data']['code'] == 0
    #     assert res.json()['data']['message'] == '登录成功'
    #     assert res.json()['data']['result']['userId'] == '2041199'
    #     assert res.json()['data']['result']['uName'] == '157****0000'
    #     assert re.match('KYYLT_2041199_', res.json()['data']['result']['token'])

    def test_get_code(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_code.yaml'))
        res = LogIn().login(data)
        print(res.json())

    def test_login_success(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/login.yaml'))[0]
        res = LogIn().login(data)
        print(res.json())

    def test_login_fail(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/login.yaml'))[1]
        res = LogIn().login(data)
        print(res.json())
