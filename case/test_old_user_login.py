import re

from basecase.basecase import BaseCase


class TestOldUserLogin(BaseCase):
    def test_old_user_login(self):
        res = self.old_user_login.olduserlogin()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['sex']))
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', res.json()['data']['ctime'])
        assert re.search(r'\d+', str(res.json()['data']['sex']))
        assert re.search(r'\w+', res.json()['data']['channelCode'])
