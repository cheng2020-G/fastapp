from basecase.basecase import BaseCase


class TestRank(BaseCase):
    def test_rank(self):
        res = self.rank.rank()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
