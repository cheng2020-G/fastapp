from basecase.basecase import BaseCase


class TestLastChapter(BaseCase):
    def test_last_chapter(self):
        res = self.last_chapter.last_chapter()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
