import re

from basecase.basecase import BaseCase


class TestSearchKeyWords(BaseCase):
    def test_search_keywords(self):
        res = self.search_keywords.search_keywords()
        print(res.json())
        print('requestId:' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        # assert re.search('[.+?]]', res.json()['data']['keywordDefault'])
