from basecase.basecase import BaseCase


class TestPush(BaseCase):
    def test_push(self):
        res = self.push.push()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
