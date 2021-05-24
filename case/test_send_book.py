from basecase.basecase import BaseCase


class TestSendBook(BaseCase):
    def test_send_book_success(self):
        res = self.send_book.send_book_success()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200

    def test_send_book_fail(self):
        res = self.send_book.send_book_fail()
        print('请求uir：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 4200
        assert res.json()['isExpire'] == 1
        assert res.json()['retMsg'] == '没有权限'
