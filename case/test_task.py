from basecase.basecase import BaseCase


class TestTask(BaseCase):
    def test_task(self):
        res = self.task.task()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['code'] == 103
        assert res.json()['data']['message'] == '奖励已领取'
