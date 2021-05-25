import re

from basecase.basecase import BaseCase


class TestGetCoupon(BaseCase):
    def test_get_coupon(self):
        res = self.get_coupon.get_coupon()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 1
        assert res.json()['isExpire'] == 1
        assert re.search(r'\w+', res.json()['retMsg'])