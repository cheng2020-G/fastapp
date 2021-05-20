from basecase.basecase import BaseCase


class TestAppStart(BaseCase):
    def test_app_start(self):
        res = self.app_start.app_start()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
