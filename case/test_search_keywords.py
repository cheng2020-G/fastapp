import re

from basecase.basecase import BaseCase


class TestSearchKeyWords(BaseCase):
    def test_search_keywords(self):
        res = self.search_keywords.search_keywords()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('.+?', str(res.json()['data']['keywordDefault']))
