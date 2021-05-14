from basecase.basecase import BaseCase


class TestFrontError(BaseCase):
    def test_front_error(self):
        res = self.fronterror.front_error()
        print(res.json())
        assert res.status_code == 200
