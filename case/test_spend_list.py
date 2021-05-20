from basecase.basecase import BaseCase


class TestSpendList(BaseCase):
    def test_spend_list(self):
        res = self.spend_list.spend_list()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['isExist'] == 2
