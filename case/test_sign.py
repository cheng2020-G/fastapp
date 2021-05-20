import re

from basecase.basecase import BaseCase


class TestSign(BaseCase):
    def test_sign(self):
        res = self.sign.sign()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\d', str(res.json()['data']['isSign']))
        assert re.search(r'\d+', str(res.json()['data']['continueDay']))
        assert re.search(r'', str(res.json()['data']['signWidget']['type']))
