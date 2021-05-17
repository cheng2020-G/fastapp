from basecase.basecase import BaseCase


class TestVivoMessage(BaseCase):
    def test_vivo_message(self):
        res = self.vivomessage.vivo_message()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        print(res.json()['data']['templateIds'])
        assert res.status_code == 200
