from basecase.basecase import BaseCase


class TestUserCoupon(BaseCase):
    def test_user_coupon(self):
        res = self.usercoupon.user_coupon()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
