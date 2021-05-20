import re

from basecase.basecase import BaseCase


class TestUserCoupon(BaseCase):
    def test_user_coupon_2203(self):
        res = self.user_coupon.user_coupon()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d+', str(res.json()['data']['counponVoList'][0]['id']))
        assert re.search(r'\d', str(res.json()['data']['counponVoList'][0]['type']))
        assert re.search(r'\d+', str(res.json()['data']['counponVoList'][0]['discount']))
        assert re.search(r'\d', str(res.json()['data']['counponVoList'][0]['premise']))
        assert re.search(r'\d{4}-\d{2}-\d{2}', res.json()['data']['counponVoList'][0]['expiryDate'])
        assert re.search(r'\d+', str(res.json()['data']['counponVoList'][0]['lastId']))
