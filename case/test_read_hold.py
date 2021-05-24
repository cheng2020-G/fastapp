from basecase.basecase import BaseCase


class TestReadHold(BaseCase):
    def test_read_hold(self):
        res = self.read_hold.read_hold()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['styleType'] == 0
