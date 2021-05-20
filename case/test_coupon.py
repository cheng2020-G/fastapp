from basecase.basecase import BaseCase


class TestCoupon(BaseCase):
    def test_coupon(self):
        res = self.coupon.coupon()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
