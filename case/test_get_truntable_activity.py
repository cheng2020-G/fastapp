from basecase.basecase import BaseCase


class TestGetTruntableActivity(BaseCase):
    def test_get_truntable_activity(self):
        res = self.getturntableactivity.get_truntable_activity()
        print(res.json())
        assert res.status_code == 200
