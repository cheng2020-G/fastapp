from basecase.basecase import BaseCase


class TestUserAuthorize(BaseCase):
    def test_user_authorize(self):
        res = self.userauthorize.userauthorize()
        print(res.json())
        assert res.status_code == 200
