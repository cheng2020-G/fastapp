from basecase.basecase import BaseCase


class TestCateGorySecond(BaseCase):
    def test_cate_gory_second(self):
        res = self.categorysecond.categorysecond()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
