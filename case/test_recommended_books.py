from basecase.basecase import BaseCase


class TestRecommendBooks(BaseCase):
    def test_recommended_books(self):
        res = self.recommendedbooks.recommendedbooks()
        print(res.json())
        assert res.status_code == 200