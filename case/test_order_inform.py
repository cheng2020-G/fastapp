from basecase.basecase import BaseCase


class TestOrderInform(BaseCase):
    def test_order_inform(self):
        res = self.orderinform.order_inform()
        print(res.json())
        assert res.status_code == 200