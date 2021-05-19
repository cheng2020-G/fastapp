import re

from basecase.basecase import BaseCase


class TestCollectCards(BaseCase):
    def test_collect_cards(self):
        res = self.getcollect_cards.get_collect_cards()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('.+?', res.json()['data']['message'])
