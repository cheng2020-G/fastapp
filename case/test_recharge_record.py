from basecase.basecase import BaseCase


class TestRechargeRecord(BaseCase):
    def test_recharge_record(self):
        res = self.rechargerecord.recharge_record()
        print(res.json())
        assert res.status_code == 200
