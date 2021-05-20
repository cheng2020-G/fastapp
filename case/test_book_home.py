from basecase.basecase import BaseCase


class TestBookHome(BaseCase):
    def test_book_home(self):
        res = self.book_home.book_home()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
