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
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['author']))
        assert re.search(r'http://\w+', str(res.json()['data']['section'][0]['coverWap']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['clickNum']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['totalWordSize']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['bookName']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['introduction']))
        assert re.search(r'\d+', str(res.json()['data']['section'][0]['bookId']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['status']))

