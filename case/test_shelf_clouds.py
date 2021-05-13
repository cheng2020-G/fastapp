from basecase.basecase import BaseCase


class TestShelfClouds(BaseCase):
    def test_shelf_clouds(self):
        res = self.shelfclouds.shelfclouds()
        print(res.json())
        assert res.status_code == 200
