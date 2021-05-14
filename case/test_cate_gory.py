from basecase.basecase import BaseCase


class TestCateGory(BaseCase):
    def test_cate_gory(self):
        res = self.category.category()
        print(res.json())
        assert res.status_code == 200
