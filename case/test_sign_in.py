import re

from basecase.basecase import BaseCase


class TestSignIn(BaseCase):
    def test_sign_in(self):
        res = self.sign_in.sgin_in()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\d', str(res.json()['data']['awardValidity']))
        assert re.search(r'\d+', str(res.json()['data']['signWidget']['id']))
        assert re.search(r'', str(res.json()['data']['signWidget']['type']))
        assert re.search(r'http://\S+', res.json()['data']['signWidget']['imgUrl'])
        assert re.search(r'http://\S+', res.json()['data']['signWidget']['actUrl'])
        assert re.search(r'\S+', res.json()['data']['signWidget']['actText'])
        assert re.search(r'\d+', str(res.json()['data']['signWidget']['operationInfo']['id']))
        assert re.search(r'\w+', str(res.json()['data']['signWidget']['operationInfo']['name']))
        # assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d:', res.json()['data']['signWidget']['operationInfo']['startTime'])
        # assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d:', res.json()['data']['signWidget']['operationInfo']['endTime'])
        assert re.search(r'\d+', str(res.json()['data']['signWidget']['userTacticsVo']['tacticsId']))
