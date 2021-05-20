from basecase.basecase import BaseCase
import re


class TestLogIN(BaseCase):
    def test_get_code(self):
        res = self.get_code.get_code()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200

    def test_login(self):
        res = self.login.login()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        print('token: ' + res.json()['data']['result']['token'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['code'] == 0
        assert res.json()['data']['message'] == '登录成功'
        assert res.json()['data']['result']['userId'] == '2041199'
        assert res.json()['data']['result']['uName'] == '157****0000'
        assert re.match('KYYLT_2041199_', res.json()['data']['result']['token'])
