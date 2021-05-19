import re

from basecase.basecase import BaseCase


class TestVipActivity(BaseCase):
    def test_vip_activity(self):
        res = self.vip_activity.vip_activity()
        print('requestId' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['data']['id'] == 717
        assert res.json()['data']['isFollow'] == 1
        assert res.json()['data']['rechargeType'] == 0
        assert re.search('\w+', res.json()['data']['name'])
        assert re.search('#([0-9a-fA-F]{6})', res.json()['data']['bgColor'])
        assert re.search('#([0-9a-fA-F]{6})', res.json()['data']['fontColor'])
        assert re.search('\w+', res.json()['data']['rule'])
        assert re.search('http://\S+', res.json()['data']['imageOne'])
        assert re.search('http://\S+', res.json()['data']['imageTwo'])
        assert re.search('\d{4}.\d{2}.\d{2}.\s\d{2}:\d{2}', res.json()['data']['beginTime'])
        assert re.search('\d{4}.\d{2}.\d{2}.\s\d{2}:\d{2}', res.json()['data']['endTime'])
