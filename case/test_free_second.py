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
        for i in res.json()['data']['section']:
            print(i)
            assert re.search(r'\w+', str(i['author']))
            assert re.search(r'http://\w+', str(i['coverWap']))
            assert re.search(r'\w+', str(i['clickNum']))
            assert re.search(r'\w+', str(i['totalWordSize']))
            assert re.search(r'\w+', str(i['bookName']))
            assert re.search(r'\w+', str(i['introduction']))
            assert re.search(r'\d+', str(i['bookId']))
            assert re.search(r'\w+', str(i['status']))
