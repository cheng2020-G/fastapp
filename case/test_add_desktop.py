from basecase.basecase import BaseCase


class TestAddDesktop(BaseCase):
    def test_add_desktop(self):
        res = self.add_desktop.add_desktop()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['status'] == 2
