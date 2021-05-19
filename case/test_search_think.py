from basecase.basecase import BaseCase


class TestSearchThink(BaseCase):
    def test_search_think(self):
        res = self.search_think.search_think()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
