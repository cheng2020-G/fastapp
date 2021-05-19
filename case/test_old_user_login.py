from basecase.basecase import BaseCase


class TestOldUserLogin(BaseCase):
    def test_old_user_login(self):
        res = self.old_user_login.olduserlogin()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
