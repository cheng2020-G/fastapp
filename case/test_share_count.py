from basecase.basecase import BaseCase


class TestShareCount(BaseCase):
    def test_share_count(self):
        res = self.share_count.share_count()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
