import re

from basecase.basecase import BaseCase


class TestRank(BaseCase):
    def test_rank(self):
        res = self.rank.rank()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['isMore'] == 0
        assert re.search(r'\d', str(res.json()['data']['rankData'][0]['rankType']))
        assert re.search(r'\w+', res.json()['data']['rankData'][0]['rankTypeName'])
        assert re.search(r'\d', str(res.json()['data']['rankData'][0]['subList'][0]['id']))
        assert re.search(r'\w+', res.json()['data']['rankData'][0]['subList'][0]['name'])
        assert re.search(r'\d+', res.json()['data']['rankBook'][0]['bookId'])
        assert re.search(r'\w+', res.json()['data']['rankBook'][0]['bookName'])
        assert re.search(r'\w+', res.json()['data']['rankBook'][0]['author'])
        assert re.search(r'http://\w+', res.json()['data']['rankBook'][0]['coverWap'])
        assert re.search(r'.+?', res.json()['data']['rankBook'][0]['introduction'])
        assert re.search(r'.+?', res.json()['data']['rankBook'][0]['clickNum'])
