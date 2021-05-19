from basecase.basecase import BaseCase


class TestAddDesktop(BaseCase):
    def test_add_desktop(self):
        res = self.add_desktop.add_desktop()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
