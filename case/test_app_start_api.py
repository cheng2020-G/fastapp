from basecase.basecase import BaseCase


class TestAppStartApi(BaseCase):
    def test_app_start_api(self):
        res = self.appstartapi.app_start_api()
        print(res.json())
        assert res.status_code == 200