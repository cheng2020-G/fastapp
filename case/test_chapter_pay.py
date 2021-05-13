import yaml

from basecase.basecase import BaseCase


class TestChapterPay(BaseCase):
    def test_chapter_pay(self):
        res = self.chapterpay.chapter_pay()
        print(res.json())
        assert res.status_code == 200
