from basecase.basecase import BaseCase


class TestShareCount(BaseCase):
    def test_share_count(self):
        res = self.sharecount.share_count()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
