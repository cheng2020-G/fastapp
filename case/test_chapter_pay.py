import yaml

from basecase.basecase import BaseCase


class TestChapterPay(BaseCase):
    def test_chapter_pay(self):
        res = self.chapter_pay.chapter_pay()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
