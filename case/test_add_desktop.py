from basecase.basecase import BaseCase


class TestAddDesktop(BaseCase):
    def test_add_desktop(self):
        res = self.add_desktop.add_desktop()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
