import re

from basecase.basecase import BaseCase


class TestRechargeActivity(BaseCase):
    def test_recharge_activity(self):
        res = self.recharge_activity.recharge_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d+', str(res.json()['data']['id']))
        assert re.search(r'\S+', res.json()['data']['name'])
        assert re.search(r'#\w{2}\d{4}', res.json()['data']['bgColor'])
        assert re.search(r'\w+', res.json()['data']['rule'])
        assert re.search(r'http://\w+', res.json()['data']['imageOne'])
        assert re.search(r'http://\w+', res.json()['data']['imageTwo'])
        assert re.search(r'\w+', res.json()['data']['beginTime'])
        assert re.search(r'\w+', res.json()['data']['endTime'])
        assert re.search(r'\w+', res.json()['data']['endTime'])
        assert re.search(r'\d', str(res.json()['data']['isFollow']))
        assert re.search(r'\d', str(res.json()['data']['tip']))
        assert re.search(r'\d', str(res.json()['data']['rechargeType']))
        assert re.search(r'\d', str(res.json()['data']['payWayList'][0]['from']))
        assert re.search(r'\w+', res.json()['data']['payWayList'][0]['payWay'])
        assert re.search(r'\w+', res.json()['data']['payWayList'][0]['showName'])
        assert re.search(r'\d', str(res.json()['data']['payWayList'][0]['isChecked']))
        assert re.search(r'\d', str(res.json()['data']['payWayList'][0]['sort']))
