from basecase.basecase import BaseCase


class TestGetManJianActivity(BaseCase):
    def test_get_manjian_activity(self):
        res = self.getturntableactivity.get_truntable_activity()
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['awardName'] == '话费'
