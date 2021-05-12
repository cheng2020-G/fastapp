from basecase.basecase import BaseCase


class TestGetToken(BaseCase):
    def test_get_token(self):
        token= self.token.get_token()
        print(token)
        # assert self.token.get_token()