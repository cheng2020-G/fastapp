import re

from basecase.basecase import BaseCase


class TestSearch(BaseCase):
    def test_search(self):
        res = self.search.search()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        # assert re.search('\d{1}', res.json()['data']['totalSize'])