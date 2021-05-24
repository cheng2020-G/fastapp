import re

from basecase.basecase import BaseCase


class TestPosition(BaseCase):
    def test_position(self):
        res = self.position.position()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\w+', res.json()['data']['operationInfo']['name'])
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d', res.json()['data']['operationInfo']['startTime'])
        assert re.search(r'\d+', str(res.json()['data']['operationInfo']['id']))
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d', res.json()['data']['operationInfo']['endTime'])
        assert re.search(r'\d', str(res.json()['data']['countdown']))
        assert re.search(r'\d', str(res.json()['data']['skip']))
        assert re.search(r'\d+', str(res.json()['data']['id']))
        assert re.search(r'\d+', str(res.json()['data']['userTacticsVo']['sourceId']))
        assert re.search(r'\d+', str(res.json()['data']['userTacticsVo']['tacticsId']))
        assert re.search(r'\d', str(res.json()['data']['userTacticsVo']['isDot']))
        assert re.search(r'\w+', res.json()['data']['userTacticsVo']['sourceName'])
        assert re.search(r'\w+', res.json()['data']['userTacticsVo']['tacticsName'])
