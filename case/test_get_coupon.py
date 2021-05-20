from basecase.basecase import BaseCase


class TestGetCoupon(BaseCase):
    def test_get_coupon(self):
        res = self.get_coupon.get_coupon()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
