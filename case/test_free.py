from basecase.basecase import BaseCase


class TestFree(BaseCase):
    def test_free(self):
        res = self.free.free()
        print(res.json())
        assert res.status_code == 200
