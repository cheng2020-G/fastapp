import re

from basecase.basecase import BaseCase


class TestUserCenter(BaseCase):
    def test_user_center(self):
        res = self.user_center.user_center()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\d{7}', res.json()['data']['user']['userId'])
        assert re.search(r'\d', str(res.json()['data']['user']['sex']))
        assert re.search(r'\d{3}\*\*\*\*\d{4}', str(res.json()['data']['user']['nickName']))
        assert re.search(r'\d+', str(res.json()['data']['user']['activeDate']))
        assert res.json()['data']['user']['vip'] is False
        assert re.search(r'\d+', str(res.json()['data']['amount']))
        assert re.search(r'\d+', str(res.json()['data']['award']))
        assert re.search(r'\d', str(res.json()['data']['isWxShare']))
        assert re.search(r'https://\S+', res.json()['data']['goUrl'])
        assert re.search(r'\d', str(res.json()['data']['taskFinishCount']))
        assert re.search(r'\d+', str(res.json()['data']['groupNum']))
        assert re.search(r'\d', str(res.json()['data']['autoRenew']))
        assert re.search(r'\d', str(res.json()['data']['loginPopupFlag']))
        assert re.search(r'https://\S+', res.json()['data']['zhiChiUrl'])
        assert re.search(r'lv\d+', res.json()['data']['gradeNo'])
        assert re.search(r'\w+', res.json()['data']['gradeName'])
        assert res.json()['data']['isReceive'] == 1
        assert re.search(r'\d+', str(res.json()['data']['gradeAward']))
