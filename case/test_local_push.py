from basecase.basecase import BaseCase


class TestLocalPush(BaseCase):
    def test_local_push(self):
        res = self.local_push.local_push()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
