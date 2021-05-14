from basecase.basecase import BaseCase


class TestUserAuthorize(BaseCase):
    def test_user_authorize(self):
        res = self.userauthorize.userauthorize()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
