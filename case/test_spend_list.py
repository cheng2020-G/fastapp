from basecase.basecase import BaseCase


class TestSpendList(BaseCase):
    def test_spend_list(self):
        res = self.spendlist.spend_list()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
