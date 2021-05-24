from basecase.basecase import BaseCase


class TestReadTime(BaseCase):
    def test_read_time(self):
        res = self.read_time.read_time()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['data']['totalReadDuration'] == 1
