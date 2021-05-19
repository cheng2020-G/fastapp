from basecase.basecase import BaseCase


class TestCateGory(BaseCase):
    def test_cate_gory(self):
        res = self.cate_gory.cate_gory()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
