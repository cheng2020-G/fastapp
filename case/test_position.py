from basecase.basecase import BaseCase


class TestPosition(BaseCase):
    def test_position(self):
        res = self.position.position()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
