import re

from basecase.basecase import BaseCase


class TestLogOut(BaseCase):
    def test_logout(self):
        res = self.logout.logout()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['code'] == 1004
        assert re.search(r'\w+', res.json()['data']['msg'])
