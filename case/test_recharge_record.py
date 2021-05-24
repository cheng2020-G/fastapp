import re

from basecase.basecase import BaseCase


class TestRechargeRecord(BaseCase):
    def test_recharge_record(self):
        res = self.recharge_record.recharge_record()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['isExist']))
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', res.json()['data']['records'][0]['ctime'])
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', res.json()['data']['records'][0]['reTime'])
        assert re.search(r'\w+', res.json()['data']['records'][0]['title'])
        assert re.search(r'\w+', res.json()['data']['records'][0]['money'])
        assert re.search(r'\w+', res.json()['data']['records'][0]['remain'])
        assert re.search(r'\d', str(res.json()['data']['records'][0]['useStatus']))
