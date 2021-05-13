from basecase.basecase import BaseCase


class TestOldUserLogin(BaseCase):
    def test_old_user_login(self):
        res = self.olduserlogin.olduserlogin()
        print(res.json())
        assert res.status_code == 200
