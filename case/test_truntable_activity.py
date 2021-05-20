from basecase.basecase import BaseCase


class TestTurntableActivity(BaseCase):
    def test_turntable_activity(self):
        res = self.turntable_activity.turntable_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
