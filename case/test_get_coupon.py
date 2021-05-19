from basecase.basecase import BaseCase


class TestGetCoupon(BaseCase):
    def test_get_coupon(self):
        res = self.get_coupon.get_coupon()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
