import re

from basecase.basecase import BaseCase


class TestFree(BaseCase):
    def test_free(self):
        res = self.free.free()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert re.search(r'\d', str(res.json()['data']['page']))
        assert re.search(r'\d', str(res.json()['data']['section'][0]['id']))
        assert re.search(r'\d', str(res.json()['data']['section'][0]['template']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['title']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['type']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['imgUrl']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['author']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['resFormat']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['action']['dataId']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['action']['title']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['action']['type']))
        assert re.search(r'\d+', str(res.json()['data']['section'][0]['items'][0]['id']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['title']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['desc']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['bookMark']))

