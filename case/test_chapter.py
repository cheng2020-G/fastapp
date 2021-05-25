import re

from basecase.basecase import BaseCase


class TestChapter(BaseCase):
    def test_chapter(self):
        res = self.chapter.chapter()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d+', res.json()['data']['chapterList'][0]['chapterId'])
        assert re.search(r'\w+', res.json()['data']['chapterList'][0]['chapterName'])
        assert re.search(r'\d', res.json()['data']['chapterList'][0]['isCharge'])
        assert re.search(r'\d', str(res.json()['data']['chapterList'][0]['chapterIndex']))
        assert re.search(r'\d+', str(res.json()['data']['blockList'][0]['endId']))
        assert re.search(r'\d+', str(res.json()['data']['blockList'][0]['startId']))
        assert re.search(r'\w+', str(res.json()['data']['blockList'][0]['tip']))
        assert re.search(r'\d', str(res.json()['data']['index']))
        assert re.search(r'\d+', str(res.json()['data']['totalChapters']))
