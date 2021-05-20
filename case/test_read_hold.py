from basecase.basecase import BaseCase


class TestReadHold(BaseCase):
    def test_read_hold(self):
        res = self.read_hold.read_hold()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
