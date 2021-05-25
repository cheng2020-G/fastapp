import re

from basecase.basecase import BaseCase


class TestCollecCards(BaseCase):
    def test_collect_cards(self):
        res = self.collect_cards.collect_cards()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['id'] == 767
        assert re.search('.+?', res.json()['data']['name'])
        assert re.search('.+?', res.json()['data']['rule'])
        assert re.search('.+?', str(res.json()['data']['rollList']))
        assert re.search(r'\d', str(res.json()['data']['drawStatus']))
        assert re.search(r'\d', str(res.json()['data']['preSuccessNum']))
        assert re.search(r'\d', str(res.json()['data']['drawNum']))
        assert re.search(r'http://\w+', str(res.json()['data']['imageOne']))
        assert re.search(r'\d+', str(res.json()['data']['totalSuccessNum']))
        assert re.search(r'\d', str(res.json()['data']['cardList'][0]['isJiqi']))
        assert re.search(r'\d', str(res.json()['data']['cardList'][0]['num']))
        assert re.search(r'\w+', str(res.json()['data']['cardList'][0]['name']))
        assert re.search(r'\d', str(res.json()['data']['cardList'][0]['type']))
        assert re.search(r'http://\w+', str(res.json()['data']['imageTwo']))
        assert re.search(r'\w+', str(res.json()['data']['bgColor']))
        assert re.search(r'\d', str(res.json()['data']['tip']))
        assert re.search(r'\d+', str(res.json()['data']['id']))
        assert re.search(r'\w+', str(res.json()['data']['openDrawTime']))
        assert re.search(r'\w+', str(res.json()['data']['openDrawText']))
        assert re.search(r'\d', str(res.json()['data']['cardTaskList'][0]['taskType']))
        assert re.search(r'\w+', str(res.json()['data']['cardTaskList'][0]['name']))
        assert re.search(r'\d', str(res.json()['data']['cardTaskList'][0]['receiveCount']))
        assert re.search(r'\w+', str(res.json()['data']['cardTaskList'][0]['remark']))
        assert re.search(r'\d', str(res.json()['data']['cardTaskList'][0]['totalCount']))
        assert re.search(r'\d', str(res.json()['data']['cardTaskList'][0]['taskStatus']))
