from basecase.basecase import BaseCase


class TestSign(BaseCase):
    def test_sign(self):
        res = self.sign.sign()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
