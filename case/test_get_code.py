from basecase.basecase import BaseCase


class TestGetCode(BaseCase):
    def test_get_code(self):
        res = self.getcode.get_code()
        print(res.json())
        # token = res.json()['data']['result']['token']
        # print(token)
