from basecase.basecase import BaseCase


class TestGetUserID(BaseCase):
    def test_get_userid(self):
        userId = self.user_id.get_user_id()
        print(userId.json())
        assert self.user_id.get_user_id().json()
