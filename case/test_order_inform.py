from basecase.basecase import BaseCase


class TestOrderInform(BaseCase):
    def test_order_inform(self):
        res = self.order_inform.order_inform()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
