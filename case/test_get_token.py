from basecase.basecase import BaseCase


class TestGetToken(BaseCase):
    def test_get_token(self):
        res = self.token.get_token()
        print(res.json())
        # token = res.json()['data']['result']['token']
        # print(token)
