from basecase.basecase import BaseCase


class TestRechargeList(BaseCase):
    def test_recharge_list(self):
        res = self.recharge_list.recharge_list()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
