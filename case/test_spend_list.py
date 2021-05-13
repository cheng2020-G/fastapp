from basecase.basecase import BaseCase


class TestSpendList(BaseCase):
    def test_spend_list(self):
        res = self.spendlist.spend_list()
        print(res.json())
        assert res.status_code == 200