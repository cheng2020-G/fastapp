from basecase.basecase import BaseCase


class TestGetToken(BaseCase):
    def test_get_token(self):
        self.GetToken.get_token()
        assert self.GetToken.get_token()