from basecase.basecase import BaseCase


class TestRechargeRecord(BaseCase):
    def test_recharge_record(self):
        res = self.recharge_record.recharge_record()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
