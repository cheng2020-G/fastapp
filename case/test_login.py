from basecase.basecase import BaseCase


class TestLogIN(BaseCase):
    def test_login(self):
        res = self.login.login()
        print(res.json())
        # assert res.status_code == 200