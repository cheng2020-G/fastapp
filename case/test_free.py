from basecase.basecase import BaseCase


class TestFree(BaseCase):
    def test_free(self):
        res = self.free.free()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
