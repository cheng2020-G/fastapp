from basecase.basecase import BaseCase


class TestUserCoupon(BaseCase):
    def test_user_coupon(self):
        res = self.usercoupon.user_coupon()
        print(res.json())
        assert res.status_code == 200
