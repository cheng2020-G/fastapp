from basecase.basecase import BaseCase


class TestCoupon(BaseCase):
    def test_coupon(self):
        res = self.coupon.coupon()
        print(res.json())
        assert res.status_code == 200
