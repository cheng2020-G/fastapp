from basecase.basecase import BaseCase


class TestLocalPush(BaseCase):
    def test_local_push(self):
        res = self.localpush.local_push()
        print(res.json())
        assert res.status_code == 200
