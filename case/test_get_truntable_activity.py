from basecase.basecase import BaseCase


class TestGetTruntableActivity(BaseCase):
    def test_get_truntable_activity(self):
        res = self.get_turntable_activity.get_truntable_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
