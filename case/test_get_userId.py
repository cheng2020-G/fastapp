from basecase.basecase import BaseCase


class TestGetUserID(BaseCase):
    def test_get_userid(self):
        self.GetUserId.get_user_id()
        # assert self.GetUserId.get_user_id().json()
