from basecase.basecase import BaseCase


class TestFeedback(BaseCase):
    def test_feedback(self):
        res = self.feedback.feedback()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
