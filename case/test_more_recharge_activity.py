from basecase.basecase import BaseCase


class TestMoreRechargeActivity(BaseCase):
    def test_more_recharge_activity(self):
        res = self.morerechargeactivity.more_recharge_activity()
        print(res.json())
        print('requestId：'+ res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['id'] == 735
