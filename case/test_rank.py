from basecase.basecase import BaseCase


class TestRank(BaseCase):
    def test_rank(self):
        res = self.rank.rank()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
