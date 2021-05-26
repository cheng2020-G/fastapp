import re

from basecase.basecase import BaseCase


class TestFreeSecond(BaseCase):
    def test_free_second(self):
        res = self.free_second.free_second()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['page']))
        for author in res.json()['data']['section']:
            print(author)
            assert re.search(r'\w+', str(author['author']))
        for coverWap in res.json()['data']['section']:
            assert re.search(r'http://\w+', str(coverWap['coverWap']))
        for clickNum in res.json()['data']['section']:
            assert re.search(r'\w+', str(clickNum['clickNum']))
        for totalWordSize in res.json()['data']['section']:
            assert re.search(r'\w+', str(totalWordSize['totalWordSize']))
        for bookName in res.json()['data']['section']:
            assert re.search(r'\w+', str(bookName['bookName']))
        for introduction in res.json()['data']['section']:
            assert re.search(r'\w+', str(introduction['introduction']))
        for bookId in res.json()['data']['section']:
            assert re.search(r'\d+', str(bookId['bookId']))
        for status in res.json()['data']['section']:
            assert re.search(r'\w+', str(status['status']))
        # assert re.search(r'\d+', str((for bookId in res.json()['data']['section']: return)['bookId'])
