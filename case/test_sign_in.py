from basecase.basecase import BaseCase


class TestSignIn(BaseCase):
    def test_sign_in(self):
        res = self.signin.sgin_in()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
