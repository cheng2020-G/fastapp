from basecase.basecase import BaseCase


class TestLottory(BaseCase):
    def test_lottery(self):
        res = self.lottery.lottery()
        print(res.request)
        print(res.json())
        assert res.status_code == 200
