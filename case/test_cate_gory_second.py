import re

from basecase.basecase import BaseCase


class TestCateGorySecond(BaseCase):
    def test_cate_gory_second(self):
        res = self.cate_gory_second.cate_gory_second()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        # print(res.json()['data']['books'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['isMore']))
        # assert re.search(r'\d', str(res.json()['data']['sortMark'][0]['markId']))
        # assert re.search(r'\w+', str(res.json()['data']['sortMark'][0]['title']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['author']))
        assert re.search(r'\d', str(res.json()['data']['books'][0]['resFormat']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['iconDesc']))
        assert re.search(r'http://\w+', str(res.json()['data']['books'][0]['coverWap']))
        assert re.search(r'\d', str(res.json()['data']['books'][0]['iconType']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['clickNum']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['totalWordSize']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['bookName']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['introduction']))
        assert re.search(r'\d+', str(res.json()['data']['books'][0]['bookId']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['status']))
        # assert re.search(r'\d', str(res.json()['data']['statusMark'][0]['markId']))
        # assert re.search(r'\w+', str(res.json()['data']['statusMark'][0]['title']))
