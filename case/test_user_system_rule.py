import re

from basecase.basecase import BaseCase


class TestUserSystemRule(BaseCase):
    def test_user_system_rule(self):
        res = self.user_system_rule.user_system_rule()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('.+?', str(res.json()['data']['ruleList']))
        assert re.search('lv\d', res.json()['data']['rrdList'][0]['gradeId'])
        assert re.search('\S+', res.json()['data']['rrdList'][0]['gradeName'])
        assert re.search('\d', str(res.json()['data']['rrdList'][0]['exp']))
