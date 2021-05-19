from basecase.basecase import BaseCase


class TestUpDateUserInfo(BaseCase):
    def test_update_user_info(self):
        res = self.update_user_info.update_user_info()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
