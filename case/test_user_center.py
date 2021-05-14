from basecase.basecase import BaseCase


class TestUserCenter(BaseCase):
    def test_user_center(self):
        res = self.usercenter.usercenter()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
