from basecase.basecase import BaseCase


class TestBookDetails(BaseCase):
    def test_book_details(self):
        res = self.bookdetails.bookdetails()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
