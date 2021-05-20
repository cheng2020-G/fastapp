import re

from basecase.basecase import BaseCase


class TestSearch(BaseCase):
    def test_search(self):
        res = self.search.search()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('\d+', str(res.json()['data']['totalSize']))
