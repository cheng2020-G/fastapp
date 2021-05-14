from basecase.basecase import BaseCase


class TestBookHome(BaseCase):
    def test_book_home(self):
        res = self.bookhome.book_home()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
