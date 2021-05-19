from basecase.basecase import BaseCase


class TestUserAuthorize(BaseCase):
    def test_user_authorize(self):
        res = self.user_authorize.user_authorize()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
