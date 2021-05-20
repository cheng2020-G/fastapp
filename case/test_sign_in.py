from basecase.basecase import BaseCase


class TestSignIn(BaseCase):
    def test_sign_in(self):
        res = self.sign_in.sgin_in()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
