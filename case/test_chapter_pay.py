import yaml

from basecase.basecase import BaseCase


class TestChapterPay(BaseCase):
    def test_chapter_pay(self):
        res = self.chapter_pay.chapter_pay()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
