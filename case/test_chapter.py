from basecase.basecase import BaseCase


class TestChapter(BaseCase):
    def test_chapter(self):
        res = self.chapter.chapter()
        print(res.json())
        assert res.status_code == 200