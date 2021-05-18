import re

from basecase.basecase import BaseCase


class TestUserSystemRule(BaseCase):
    def test_user_system_rule(self):
        res = self.usersystemrule.user_system_rule()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        # assert re.search('[.+?]', res.json()['data']['ruleList'])
        assert re.search('lv\d', res.json()['data']['rrdList'][0]['gradeId'])
        assert re.search('\S+', res.json()['data']['rrdList'][0]['gradeName'])
        assert re.search('\d', str(res.json()['data']['rrdList'][0]['exp']))
