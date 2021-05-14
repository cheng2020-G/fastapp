from basecase.basecase import BaseCase


class TestFreeSecond(BaseCase):
    def test_free_second(self):
        res = self.freesecond.free_second()
        print(res.json())
        assert res.status_code == 200
