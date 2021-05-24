from basecase.basecase import BaseCase


class TestAppStartApi(BaseCase):
    def test_app_start_api(self):
        res = self.app_start_api.app_start_api()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['code'] == 1
