import re

from basecase.basecase import BaseCase


class TestUserSystem(BaseCase):
    def test_user_system(self):
        res = self.user_system.user_system()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search('\d{7}', res.json()['data']['userId'])
        assert re.search('lv\d', res.json()['data']['gradeNo'])
        assert re.search('\S+', res.json()['data']['gradeName'])
        assert re.search(r'\d+', str(res.json()['data']['totalExp']))
        assert re.search(r'\d+', str(res.json()['data']['isLast']))
        assert re.search(r'\d', str(res.json()['data']['nextExp']))
        assert re.search(r'\d', str(res.json()['data']['rightNum']))
        assert re.search(r'\w+', str(res.json()['data']['gradeTip']))
        assert re.search(r'\d', str(res.json()['data']['rightList'][0]['isFlag']))
        assert re.search(r'\d', str(res.json()['data']['rightList'][0]['num']))
        assert re.search(r'\d', str(res.json()['data']['rightList'][0]['type']))
        assert re.search(r'\w+', res.json()['data']['rightList'][0]['rightName'])
        assert re.search(r'.+?', res.json()['data']['rightList'][0]['rightDesc'])
        assert re.search(r'lv\d', res.json()['data']['rightList'][0]['rightDescList'][0]['gradeId'])
        assert re.search(r'\S+', res.json()['data']['rightList'][0]['rightDescList'][0]['gradeName'])
        assert re.search(r'\S+', res.json()['data']['rightList'][0]['rightDescList'][0]['awardDesc'])
        assert re.search(r'\d+', str(res.json()['data']['rightList'][0]['rightDescList'][0]['award']))
        assert re.search(r'\d', str(res.json()['data']['rightList'][0]['rightDescList'][0]['status']))