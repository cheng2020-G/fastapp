from basecase.basecase import BaseCase


class TestMoreRechargeActivity(BaseCase):
    def test_more_recharge_activity(self):
        res = self.more_recharge_activity.more_recharge_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['id'] == 735
