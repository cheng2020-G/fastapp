import re

from basecase.basecase import BaseCase


class TestGetManJianActivity(BaseCase):
    def test_get_manjian_activity(self):
        res = self.get_turntable_activity.get_truntable_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['awardName'] == '话费'
        assert re.search(r'\d+', str(res.json()['data']['awardId']))
        assert re.search(r'\d', str(res.json()['data']['awardType']))
        assert re.search(r'http://\w+', str(res.json()['data']['awardImg']))
        assert re.search(r'\d+', str(res.json()['data']['awardCount']))
        assert re.search(r'.+?', str(res.json()['data']['awardReferObj']))
        assert re.search(r'\w+', str(res.json()['data']['mobileFeeRecordCode']))
        assert re.search(r'\d', str(res.json()['data']['drawedTimes']))
        assert re.search(r'\d', str(res.json()['data']['gradeDrawCount']))
        assert re.search(r'\d', str(res.json()['data']['awardType']))
