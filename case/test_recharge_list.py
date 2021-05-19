from basecase.basecase import BaseCase


class TestRechargeList(BaseCase):
    def test_recharge_list(self):
        res = self.recharge_list.recharge_list()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
