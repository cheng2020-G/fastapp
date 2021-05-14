from basecase.basecase import BaseCase


class TestRechargeList(BaseCase):
    def test_recharge_list(self):
        res = self.rechargelist.rechargelist()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
