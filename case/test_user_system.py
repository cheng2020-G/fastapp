import re

from basecase.basecase import BaseCase


class TestUserSystem(BaseCase):
    def test_user_system(self):
        res = self.usersystem.user_system()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('\d{7}', res.json()['data']['userId'])
