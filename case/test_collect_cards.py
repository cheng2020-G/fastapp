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
