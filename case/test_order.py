from basecase.basecase import BaseCase


class TestOrder(BaseCase):
    def test_order_success(self):
        res = self.order.order_success()
        print(res.json())
        assert res.status_code == 200

    def test_order_fail(self):
        res = self.order.order_fail()
        print(res.json())
        assert res.status_code == 200
