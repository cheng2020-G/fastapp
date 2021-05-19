from basecase.basecase import BaseCase


class TestShelfClouds(BaseCase):
    def test_shelf_clouds(self):
        res = self.shelf_clouds.shelf_clouds()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
