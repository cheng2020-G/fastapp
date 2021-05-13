from basecase.basecase import BaseCase


class TestReadBegin(BaseCase):
    def test_read_begin(self):
        res = self.readbegin.read_begin()
        print(res.json())
        assert res.status_code == 200