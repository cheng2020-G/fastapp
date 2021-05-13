from basecase.basecase import BaseCase


class TestLogOut(BaseCase):
    def test_logout(self):
        res = self.logout.logout()
        print(res.json())
        assert res.status_code == 200
