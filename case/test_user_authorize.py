from basecase.basecase import BaseCase


class TestUserAuthorize(BaseCase):
    def test_user_authorize(self):
        res = self.user_authorize.user_authorize()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
