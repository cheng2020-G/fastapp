from basecase.basecase import BaseCase
import re


class TestGetCode(BaseCase):
    def test_get_code(self):
        res = self.get_code.get_code()
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        # token = res.json()['data']['result']['token']
        # print(token)
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('您的安全验证码是：', res.json()['data']['mtKeyword'])
        assert re.search(r'.+?', res.json()['data']['rule'])
        assert res.json()['data']['result'] == '1'
