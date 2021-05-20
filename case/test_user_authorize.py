import re

from basecase.basecase import BaseCase


class TestUserAuthorize(BaseCase):
    def test_user_authorize(self):
        res = self.user_authorize.user_authorize()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['sex']))
        assert re.search(r'\d+', str(res.json()['data']['userId']))
        assert re.search(r'\w+', res.json()['data']['channelCode'])
