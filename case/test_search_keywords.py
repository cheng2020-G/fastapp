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
        assert re.search(r'\d+', res.json()['data']['recommendHots'][0]['bookId'])
        assert re.search(r'\w+', res.json()['data']['recommendHots'][0]['bookName'])
        assert re.search(r'\w+', res.json()['data']['recommendHots'][0]['author'])
        assert re.search(r'.+?', res.json()['data']['recommendHots'][0]['introduction'])
        assert re.search(r'http://\S+', res.json()['data']['recommendHots'][0]['coverWap'])
        assert re.search('.+?', res.json()['data']['recommendHots'][0]['hot'])
        assert res.json()['data']['isMore'] == 0
        assert res.json()['data']['rankId'] == '3'
        assert re.search('.+?', str(res.json()['data']['keywordDefault']))

