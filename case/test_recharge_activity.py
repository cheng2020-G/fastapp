from basecase.basecase import BaseCase


class TestRechargeActivity(BaseCase):
    def test_recharge_activity(self):
        res = self.rechargeactivity.recharge_activity()
        print(res.json())
        assert res.status_code == 200
