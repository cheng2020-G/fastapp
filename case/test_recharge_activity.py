from basecase.basecase import BaseCase


class TestRechargeActivity(BaseCase):
    def test_recharge_activity(self):
        res = self.recharge_activity.recharge_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
