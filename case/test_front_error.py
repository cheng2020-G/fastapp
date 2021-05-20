from basecase.basecase import BaseCase


class TestFrontError(BaseCase):
    def test_front_error(self):
        res = self.front_error.front_error()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
