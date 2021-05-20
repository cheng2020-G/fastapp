from basecase.basecase import BaseCase


class TestPush(BaseCase):
    def test_push(self):
        res = self.push.push()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
