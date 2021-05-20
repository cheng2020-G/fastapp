from basecase.basecase import BaseCase


class TestRecommendBooks(BaseCase):
    def test_recommended_books(self):
        res = self.recommended_books.recommended_books()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
