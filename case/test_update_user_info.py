from basecase.basecase import BaseCase


class TestUpDateUserInfo(BaseCase):
    def test_update_user_info(self):
        res = self.update_user_info.update_user_info()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['code'] == 1
