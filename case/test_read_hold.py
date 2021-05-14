from basecase.basecase import BaseCase


class TestReadHold(BaseCase):
    def test_read_hold(self):
        res = self.readhold.readhold()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
