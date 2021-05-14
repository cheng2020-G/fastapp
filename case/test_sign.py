from basecase.basecase import BaseCase


class TestSign(BaseCase):
    def test_sign(self):
        res = self.sign.sign()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
