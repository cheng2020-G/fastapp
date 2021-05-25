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
        assert re.search(r'\d', str(res.json()['data']['consumeReturns'][0]['awardId']))
        assert re.search(r'\d', str(res.json()['data']['jumpType']))
        assert re.search(r'http://\w+', str(res.json()['data']['buttonImg']))
        assert re.search(r'\w+', str(res.json()['data']['color']))
        assert re.search(r'\d+', str(res.json()['data']['consumeReturns'][0]['activityId']))
        assert re.search(r'\d', str(res.json()['data']['consumeReturns'][0]['awardId']))
        assert re.search(r'\w+', str(res.json()['data']['consumeReturns'][0]['couponName']))
        assert re.search(r'\d', str(res.json()['data']['consumeReturns'][0]['premise']))
        assert re.search(r'\d', str(res.json()['data']['consumeReturns'][0]['awardNum']))
        assert re.search(r'\d', str(res.json()['data']['consumeReturns'][0]['awardStatus']))
        assert re.search(r'\w+', str(res.json()['data']['activityName']))
        assert re.search(r'\w+', str(res.json()['data']['activityTime']))
        assert re.search(r'http://\w+', str(res.json()['data']['upImg']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['readAmout']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['author']))
        assert re.search(r'http://\w+', str(res.json()['data']['books'][0]['coverImage']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['bookName']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['introduction']))
        assert re.search(r'\d+', str(res.json()['data']['books'][0]['bookId']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['status']))
        assert re.search(r'\d', str(res.json()['data']['totalConsume']))
        assert re.search(r'http://\w+', str(res.json()['data']['downImg']))
        assert re.search(r'http://\w+', str(res.json()['data']['columnImg']))
        assert re.search(r'\d+', str(res.json()['data']['sysTime']))
        assert re.search(r'\d', str(res.json()['data']['tip']))
        assert re.search(r'\d+', str(res.json()['data']['endTime']))
        assert re.search(r'\d+', str(res.json()['data']['beginTime']))
        assert re.search(r'\w+', str(res.json()['data']['activityRule']))
