from basecase.basecase import BaseCase


class TestAppStartApi(BaseCase):
    def test_app_start_api(self):
        res = self.app_start_api.app_start_api()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
