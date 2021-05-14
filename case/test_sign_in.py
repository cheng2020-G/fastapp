from basecase.basecase import BaseCase


class TestSignIn(BaseCase):
    def test_sign_in(self):
        res = self.signin.sgin_in()
        print(res.json())
        assert res.status_code == 200
