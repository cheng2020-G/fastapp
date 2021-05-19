from basecase.basecase import BaseCase


class TestReadTime(BaseCase):
    def test_read_time(self):
        res = self.read_time.read_time()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
