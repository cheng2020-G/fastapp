from basecase.basecase import BaseCase


class TestAppStart(BaseCase):
    def test_app_start(self):
        res = self.appstart.app_start()
        print(res.json())
        assert res.status_code == 200