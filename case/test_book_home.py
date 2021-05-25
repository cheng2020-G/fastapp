import re

from basecase.basecase import BaseCase


class TestBookHome(BaseCase):
    def test_book_home(self):
        res = self.book_home.book_home()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['page']))
        assert re.search(r'\d', str(res.json()['data']['channelId']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['template']))
        assert re.search(r'\d+', str(res.json()['data']['section'][0]['action']['dataId']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['action']['title']))
        assert re.search(r'\d', str(res.json()['data']['section'][0]['action']['type']))
        assert re.search(r'\d', str(res.json()['data']['section'][0]['id']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['title']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['type']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['imgUrl']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['author']))
        assert re.search(r'\d', str(res.json()['data']['section'][0]['items'][0]['resFormat']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['iconDesc']))
        assert re.search(r'\d+', str(res.json()['data']['section'][0]['items'][0]['iconType']))
        assert re.search(r'\d+', str(res.json()['data']['section'][0]['items'][0]['action']['dataId']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['action']['title']))
        assert re.search(r'\d', str(res.json()['data']['section'][0]['items'][0]['action']['type']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['clickNum']))
        assert re.search(r'\d+', str(res.json()['data']['section'][0]['items'][0]['id']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['title']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['desc']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['bookMark']))
        assert re.search(r'\w+', str(res.json()['data']['section'][0]['items'][0]['status']))
        assert re.search(r'\d', str(res.json()['data']['page']))
        assert re.search(r'\d', str(res.json()['data']['channelId']))
