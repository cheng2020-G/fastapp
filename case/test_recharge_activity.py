from basecase.basecase import BaseCase


class TestRechargeActivity(BaseCase):
    def test_recharge_activity(self):
        res = self.recharge_activity.recharge_activity()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
