from basecase.basecase import BaseCase


class TestPosition(BaseCase):
    def test_position(self):
        res = self.position.position()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
