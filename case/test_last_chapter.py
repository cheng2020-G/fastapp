from basecase.basecase import BaseCase


class TestLastChapter(BaseCase):
    def test_last_chapter(self):
        res = self.lastchapter.lastchapter()
        print(res.json())
        assert  res.status_code == 200