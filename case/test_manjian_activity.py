import re

from basecase.basecase import BaseCase


class TestManJianActivity(BaseCase):
    def test_manjian_activity(self):
        res = self.manjian_activity.manjian_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['consumeReturns'][0]['activityId'] == 722
        assert re.search('\d', str(res.json()['data']['consumeReturns'][0]['awardId']))
