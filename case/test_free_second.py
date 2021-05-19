from basecase.basecase import BaseCase


class TestFreeSecond(BaseCase):
    def test_free_second(self):
        res = self.free_second.free_second()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
