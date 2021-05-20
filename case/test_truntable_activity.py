import re

from basecase.basecase import BaseCase


class TestTurntableActivity(BaseCase):
    def test_turntable_activity(self):
        res = self.turntable_activity.turntable_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['id'] == 772
        assert re.search(r'.+?', res.json()['data']['name'])
        assert re.search(r'.+?', res.json()['data']['rule'])
        assert re.search(r'http://\w+', res.json()['data']['imageOne'])
        assert re.search(r'http://\w+', res.json()['data']['imageTwo'])
        assert re.search(r'\d+', str(res.json()['data']['beginTime']))
        assert re.search(r'\d+', str(res.json()['data']['endTime']))
        assert re.search(r'\d', str(res.json()['data']['consumeCount']))
        assert re.search(r'\d', str(res.json()['data']['userDrawCount']))
        assert re.search(r'\d', str(res.json()['data']['gradeDrawCount']))
        assert re.search(r'\d+', str(res.json()['data']['times']))
        assert re.search(r'\d+', str(res.json()['data']['sysTime']))
        assert re.search(r'\d+', str(res.json()['data']['userId']))
        assert re.search(r'\d+\*\*\*\d+', res.json()['data']['historyAwardList'][0]['userId'])
        assert re.search(r'\S+', res.json()['data']['historyAwardList'][0]['awardName'])
        assert re.search(r'\d', str(res.json()['data']['historyAwardList'][0]['awardType']))
