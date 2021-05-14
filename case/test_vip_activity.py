from basecase.basecase import BaseCase


class TestVipActivity(BaseCase):
    def test_vip_activity(self):
        res = self.vipactivity.vip_activity()
        print(res.json())
        assert res.status_code == 200
