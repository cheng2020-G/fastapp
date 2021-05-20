from basecase.basecase import BaseCase


class TestShelfClouds(BaseCase):
    def test_shelf_clouds(self):
        res = self.shelf_clouds.shelf_clouds()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
