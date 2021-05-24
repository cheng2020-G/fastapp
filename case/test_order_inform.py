import re

from basecase.basecase import BaseCase


class TestOrderInform(BaseCase):
    def test_order_inform(self):
        res = self.order_inform.order_inform()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['data']['result'] == 3
        assert re.search(r'\d', res.json()['data']['remain'])
