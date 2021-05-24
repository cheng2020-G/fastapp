import re

from basecase.basecase import BaseCase


class TestPresTrain(BaseCase):
    def test_pres_train(self):
        res = self.prestrain.prestrain()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'\d', str(res.json()['data']['isJp']))
        assert re.search(r'\w+', res.json()['data']['bookStatus'])
        assert re.search(r'\w+', res.json()['data']['first_reading'])
        assert re.search(r'\w+', res.json()['data']['bookFinishStatus'])
        assert re.search(r'\w+', res.json()['data']['author'])
        assert re.search(r'\w+', res.json()['data']['firstType'])
        assert re.search(r'\w+', res.json()['data']['chaptersPayType'])
        assert re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d', res.json()['data']['updateTime'])
        assert re.search(r'\d+', str(res.json()['data']['maxChapter']))
        assert re.search(r'\w+', res.json()['data']['bookName'])
        assert re.search(r'\w+', res.json()['data']['secondType'])
        assert re.search(r'False|True', str(res.json()['data']['isVip']))
        assert re.search(r'\d+', str(res.json()['data']['bookId']))
        assert re.search(r'\d', str(res.json()['data']['warnTip']))
        assert re.search(r'\d', str(res.json()['data']['SensitivityLevel']))
        assert re.search(r'\w+', res.json()['data']['payType'])
        assert re.search(r'\d', str(res.json()['data']['chapterInfo'][0]['cost']))
        assert re.search(r'\w+', res.json()['data']['chapterInfo'][0]['preChapterName'])
        assert re.search(r'\d+', str(res.json()['data']['chapterInfo'][0]['chapterId']))
        assert re.search(r'\w+', res.json()['data']['chapterInfo'][0]['chapterName'])
        assert re.search(r'\d', str(res.json()['data']['chapterInfo'][0]['isafd']))
        assert re.search(r'\w+', res.json()['data']['chapterInfo'][0]['nextChapterName'])
        assert re.search(r'\d', str(res.json()['data']['chapterInfo'][0]['chapterIndex']))
        assert re.search(r'\d+', str(res.json()['data']['chapterInfo'][0]['nextChapterId']))
        assert re.search(r'\d', str(res.json()['data']['chapterInfo'][0]['isRecoBook']))
        assert re.search(r'\d', str(res.json()['data']['chapterInfo'][0]['chapterStatus']))
        assert re.search(r'.+?', str(res.json()['data']['chapterInfo'][0]['content']))
        assert re.search(r'\d+', str(res.json()['data']['chapterInfo'][0]['preChapterId']))
        assert re.search(r'\d+', str(res.json()['data']['chaptersCoins']))
        assert re.search(r'\w+', res.json()['data']['thirdType'])
        assert re.search(r'\d', str(res.json()['data']['preloadNum']))
