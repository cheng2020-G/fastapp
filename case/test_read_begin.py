from basecase.basecase import BaseCase


class TestReadBegin(BaseCase):
    def test_read_begin(self):
        res = self.read_begin.read_begin()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
