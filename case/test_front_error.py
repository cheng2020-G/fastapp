from basecase.basecase import BaseCase


class TestFrontError(BaseCase):
    def test_front_error(self):
        res = self.front_error.front_error()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data'] == 1
