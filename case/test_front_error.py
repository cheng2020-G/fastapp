from basecase.basecase import BaseCase


class TestFrontError(BaseCase):
    def test_front_error(self):
        res = self.front_error.front_error()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
