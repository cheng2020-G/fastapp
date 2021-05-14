from basecase.basecase import BaseCase


class TestUpDateUserInfo(BaseCase):
    def test_update_user_info(self):
        res = self.updateuserinfo.updateuserinfo()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
