from basecase.basecase import BaseCase


class TestBookDetails(BaseCase):
    def test_book_details(self):
        res = self.book_details.book_details()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
