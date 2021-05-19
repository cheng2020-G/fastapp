from basecase.basecase import BaseCase


class TestBookDetails(BaseCase):
    def test_book_details(self):
        res = self.book_details.book_details()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
