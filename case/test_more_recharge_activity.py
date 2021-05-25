import re

from basecase.basecase import BaseCase


class TestMoreRechargeActivity(BaseCase):
    def test_more_recharge_activity(self):
        res = self.more_recharge_activity.more_recharge_activity()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['id'] == 735
        assert re.search(r'\d', str(res.json()['data']['isFollow']))
        assert re.search(r'\w+', str(res.json()['data']['bgColor']))
        assert re.search(r'\w+', str(res.json()['data']['name']))
        assert re.search(r'http://\w+', str(res.json()['data']['imageOne']))
        assert re.search(r'.+?', str(res.json()['data']['rule']))
        assert re.search(r'\w+', str(res.json()['data']['payWayList'][0]['showName']))
        assert re.search(r'\w+', str(res.json()['data']['payWayList'][0]['payWay']))
        assert re.search(r'\d', str(res.json()['data']['payWayList'][0]['from']))
        assert re.search(r'\d', str(res.json()['data']['payWayList'][0]['sort']))
        assert re.search(r'\d', str(res.json()['data']['payWayList'][0]['isChecked']))
        assert re.search(r'\d', str(res.json()['data']['tip']))
        assert re.search(r'\d+', str(res.json()['data']['id']))
        assert re.search(r'\w+', str(res.json()['data']['beginTime']))
        assert re.search(r'\w+', str(res.json()['data']['endTime']))
        assert re.search(r'\w+', str(res.json()['data']['payList'][0]['give']))
        assert re.search(r'[0-9]\d*.[0-9]\d*', str(res.json()['data']['payList'][0]['amountNum']))
        assert re.search(r'\w+', str(res.json()['data']['payList'][0]['amount']))
        assert re.search(r'\w+', str(res.json()['data']['payList'][0]['product']))
        assert re.search(r'\w+', str(res.json()['data']['payList'][0]['corner']))
        assert re.search(r'\d', str(res.json()['data']['payList'][0]['isHighlight']))
        assert re.search(r'\d+', str(res.json()['data']['payList'][0]['giveNum']))
        assert re.search(r'\d', str(res.json()['data']['payList'][0]['checked']))
        assert re.search(r'\d+', str(res.json()['data']['payList'][0]['payCount']))
        assert re.search(r'\d+', str(res.json()['data']['payList'][0]['id']))
        assert re.search(r'\d+', str(res.json()['data']['payList'][0]['productNum']))
        assert re.search(r'\d', str(res.json()['data']['payList'][0]['type']))
        assert re.search(r'', res.json()['data']['fontColor'])
