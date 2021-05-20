from basecase.basecase import BaseCase


class TestReadBegin(BaseCase):
    def test_read_begin(self):
        res = self.read_begin.read_begin()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
