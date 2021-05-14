from basecase.basecase import BaseCase


class TestTurntableActivity(BaseCase):
    def test_turntable_activity(self):
        res = self.turntableactivity.turntable_activity()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
