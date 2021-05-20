from basecase.basecase import BaseCase


class TestCateGory(BaseCase):
    def test_cate_gory(self):
        res = self.cate_gory.cate_gory()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
