import re

from basecase.basecase import BaseCase


class TestOrder(BaseCase):
    def test_order_success(self):
        res = self.order.order_success()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d+', str(res.json()['data']['orderNo']))
        assert re.search(r'.+?', str(res.json()['data']['reqParams']['callAliPayUrl']))

    def test_order_fail(self):
        res = self.order.order_fail()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 3309
        assert res.json()['retMsg'] == '请勿频繁提交订单'
