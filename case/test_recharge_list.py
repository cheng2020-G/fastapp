import re

from basecase.basecase import BaseCase


class TestRechargeList(BaseCase):
    def test_recharge_list(self):
        res = self.recharge_list.recharge_list()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d+', res.json()['data']['amount'])
        assert re.search(r'\d', str(res.json()['data']['puSwitch']))
        assert re.search(r'\d{3}\*\*\*\*\d{4}', res.json()['data']['nickName'])
        assert re.search(r'\d', str(res.json()['data']['isTask']))
        assert re.search(r'\d', str(res.json()['data']['isWechatPay']))
        assert re.search(r'\d+', str(res.json()['data']['userId']))
        assert re.search(r'\d+', str(res.json()['data']['userId']))
        assert re.search(r'\d', str(res.json()['data']['isFollow']))
        assert re.search(r'\d', str(res.json()['data']['autoOrder']))
        assert re.search(r'\d+', str(res.json()['data']['payListUt']['sourceId']))
        assert re.search(r'\d+', str(res.json()['data']['payListUt']['tacticsId']))
        assert re.search(r'\d', str(res.json()['data']['payListUt']['isDot']))
        assert re.search(r'\w+', str(res.json()['data']['payListUt']['sourceName']))
        assert re.search(r'\w+', str(res.json()['data']['payListUt']['tacticsName']))
        assert re.search('.+?', str(res.json()['data']['payTip']))
        assert re.search('.+?', str(res.json()['data']['products'][0]['amount']))
        assert re.search(r'\w+', str(res.json()['data']['payWays'][0]['showName']))
        assert re.search(r'\w+', str(res.json()['data']['payWays'][0]['payWay']))
        assert re.search(r'\d', str(res.json()['data']['payWays'][0]['from']))
        assert re.search(r'\d', str(res.json()['data']['payWays'][0]['isChecked']))

