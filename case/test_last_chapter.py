from basecase.basecase import BaseCase


class TestLastChapter(BaseCase):
    def test_last_chapter(self):
        res = self.last_chapter.last_chapter()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
