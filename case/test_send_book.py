from basecase.basecase import BaseCase


class TestSendBook(BaseCase):
    def test_send_book(self):
        res = self.send_book.send_book()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
