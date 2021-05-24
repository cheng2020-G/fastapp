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
        assert re.search(r'\d+', str(res.json()['data']['totalSize']))
        assert re.search(r'\d', str(res.json()['data']['searchType']))
        assert re.search(r'\d', str(res.json()['data']['isMore']))
        assert re.search(r'\d', str(res.json()['data']['rankId']))
        assert re.search(r'\d+', res.json()['data']['bookList'][0]['bookId'])
        assert re.search(r'\w+', res.json()['data']['bookList'][0]['bookName'])
        assert re.search(r'\w+', res.json()['data']['bookList'][0]['author'])
        assert re.search(r'.+?', res.json()['data']['bookList'][0]['introduction'])
        assert re.search(r'http://\w+', res.json()['data']['bookList'][0]['coverWap'])
        assert re.search(r'\S+', res.json()['data']['bookList'][0]['hot'])
