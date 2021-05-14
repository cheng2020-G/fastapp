from basecase.basecase import BaseCase


class TestFeedback(BaseCase):
    def test_feedback(self):
        res = self.feedback.feedback()
        print(res.json())
        assert res.status_code == 200
