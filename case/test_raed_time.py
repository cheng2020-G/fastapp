from basecase.basecase import BaseCase


class TestReadTime(BaseCase):
    def test_read_time(self):
        res = self.readtime.read_time()
        print(res.json())
        assert res.status_code == 200