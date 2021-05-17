import re

from basecase.basecase import BaseCase


class TestLook(BaseCase):
    def test_look(self):
        res = self.look.look()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        # assert re.match('\d', res.json()['data']['resultVideoList'][0]['id'])
