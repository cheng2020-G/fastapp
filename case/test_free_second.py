from basecase.basecase import BaseCase


class TestFreeSecond(BaseCase):
    def test_free_second(self):
        res = self.free_second.free_second()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
