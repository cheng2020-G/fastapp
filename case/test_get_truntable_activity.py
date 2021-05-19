from basecase.basecase import BaseCase


class TestGetTruntableActivity(BaseCase):
    def test_get_truntable_activity(self):
        res = self.get_turntable_activity.get_truntable_activity()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
