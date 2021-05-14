from basecase.basecase import BaseCase


class TestSendBook(BaseCase):
    def test_send_book(self):
        res = self.sendbook.sendbook()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
