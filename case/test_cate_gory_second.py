from basecase.basecase import BaseCase


class TestCateGorySecond(BaseCase):
    def test_cate_gory_second(self):
        res = self.cate_gory_second.cate_gory_second()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
