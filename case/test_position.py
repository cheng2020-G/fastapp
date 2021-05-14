from basecase.basecase import BaseCase


class TestPosition(BaseCase):
    def test_position(self):
        res = self.position.position()
        print(res.json())
        assert res.status_code == 200
