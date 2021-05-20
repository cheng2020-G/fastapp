from basecase.basecase import BaseCase


class TestOldUserLogin(BaseCase):
    def test_old_user_login(self):
        res = self.old_user_login.olduserlogin()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
