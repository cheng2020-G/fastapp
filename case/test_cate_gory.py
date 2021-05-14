from basecase.basecase import BaseCase


class TestCateGory(BaseCase):
    def test_cate_gory(self):
        res = self.category.cate_gory()
        print(res.json())
        assert res.status_code == 200
