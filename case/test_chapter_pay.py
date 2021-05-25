import re

import yaml

from basecase.basecase import BaseCase


class TestChapterPay(BaseCase):
    def test_chapter_pay(self):
        res = self.chapter_pay.chapter_pay()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['isafd']))
        assert re.search(r'\w+', str(res.json()['data']['chaptersPayType']))
        assert re.search(r'\d', str(res.json()['data']['isRecoBook']))
        assert re.search(r'\d+', str(res.json()['data']['maxChapter']))
        assert re.search(r'\w+', str(res.json()['data']['secondType']))
        assert re.search(r'\w+', str(res.json()['data']['payType']))
        assert re.search(r'\d+', str(res.json()['data']['chapterInfo'][0]['cost']))
        assert re.search(r'\d+', str(res.json()['data']['chapterInfo'][0]['chapterId']))
        assert re.search(r'\w+', str(res.json()['data']['chapterInfo'][0]['chapterName']))
        assert re.search(r'\d', str(res.json()['data']['chapterInfo'][0]['chapterStatus']))
        assert re.search(r'\w+', str(res.json()['data']['chapterInfo'][0]['content']))
        assert re.search(r'True|False', str(res.json()['data']['isInBookShelf']))
        assert re.search(r'\w+', str(res.json()['data']['thirdType']))
        assert re.search(r'\d', str(res.json()['data']['isJp']))
        assert re.search(r'\w+', str(res.json()['data']['bookStatus']))
        assert re.search(r'\w+', str(res.json()['data']['first_reading']))
        assert re.search(r'\w+', str(res.json()['data']['preChapterName']))
        assert re.search(r'\w+', str(res.json()['data']['bookFinishStatus']))
        assert re.search(r'\w+', str(res.json()['data']['author']))
        assert re.search(r'\w+', str(res.json()['data']['firstType']))
        assert re.search(r'\w+', str(res.json()['data']['nextChapterName']))
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d', str(res.json()['data']['updateTime']))
        assert re.search(r'\d', str(res.json()['data']['isAdd']))
        assert re.search(r'\w+', str(res.json()['data']['bookName']))
        assert re.search(r'True|False', str(res.json()['data']['isVip']))
        assert re.search(r'\d+', str(res.json()['data']['bookId']))
        assert re.search(r'\d', str(res.json()['data']['warnTip']))
        assert re.search(r'\d', str(res.json()['data']['SensitivityLevel']))
        assert re.search(r'\d+', str(res.json()['data']['chapterIndex']))
        assert re.search(r'\d+', str(res.json()['data']['nextChapterId']))
        assert re.search(r'\d+', str(res.json()['data']['chaptersCoins']))
        assert re.search(r'\d', str(res.json()['data']['status']))
        assert re.search(r'\d+', str(res.json()['data']['preChapterId']))
        assert re.search(r'\d', str(res.json()['data']['preloadNum']))
