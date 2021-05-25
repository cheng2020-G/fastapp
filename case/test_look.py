import re

from basecase.basecase import BaseCase


class TestLook(BaseCase):
    def test_look(self):
        res = self.look.look()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\d+', str(res.json()['data']['offset']))
        assert re.search(r'False|True', str(res.json()['data']['hasNext']))
        assert re.search(r'http://\w+', str(res.json()['data']['resultVideoList'][0]['address']))
        assert re.search(r'False|True', str(res.json()['data']['resultVideoList'][0]['inBookShelf']))
        assert re.search(r'http://\w+', str(res.json()['data']['resultVideoList'][0]['videoCoverWapp']))
        assert re.search(r'http://\w+', str(res.json()['data']['resultVideoList'][0]['coverWap']))
        assert re.search(r'\w+', str(res.json()['data']['resultVideoList'][0]['remark']))
        assert re.search(r'\d+', str(res.json()['data']['resultVideoList'][0]['id']))
        assert re.search(r'\w+', str(res.json()['data']['resultVideoList'][0]['bookName']))
        assert re.search(r'\d+', str(res.json()['data']['resultVideoList'][0]['bookId']))
