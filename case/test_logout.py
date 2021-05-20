from basecase.basecase import BaseCase


class TestLogOut(BaseCase):
    def test_logout(self):
        res = self.logout.logout()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
