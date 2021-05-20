from basecase.basecase import BaseCase


class TestLottory(BaseCase):
    def test_lottery(self):
        res = self.lottery.lottery()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
