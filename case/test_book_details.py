import re

from basecase.basecase import BaseCase


class TestBookDetails(BaseCase):
    def test_book_details(self):
        res = self.book_details.book_details()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\w+', res.json()['data']['readTips'])
        # assert re.search(r'\d+', str(res.json()['data']['chapters'][0]['chapterId']))
        # assert re.search(r'\w+', str(res.json()['data']['chapters'][0]['chapterName']))
        assert re.search(r'\d+', res.json()['data']['chapterId'])
        assert re.search(r'\w+', res.json()['data']['book']['author'])
        assert re.search(r'http://\w+', res.json()['data']['book']['coverWap'])
        assert re.search(r'\d+', str(res.json()['data']['book']['praiseNum']))
        assert re.search(r'\w+', res.json()['data']['book']['twoTypeName'])
        assert re.search(r'\w+', res.json()['data']['book']['bookTypeName'])
        assert re.search(r'\w+', res.json()['data']['book']['totalWordSize'])
        assert re.search(r'\w+', res.json()['data']['book']['bookName'])
        assert re.search(r'\w+', res.json()['data']['book']['lastChapterName'])
        assert re.search(r'\d+', res.json()['data']['book']['bookId'])
        assert re.search(r'\w+', str(res.json()['data']['book']['tagList']))
        assert re.search(r'\d', str(res.json()['data']['book']['unit']))
        assert re.search(r'\d+', str(res.json()['data']['book']['totalChapterNum']))
        assert re.search(r'\w+', str(res.json()['data']['book']['iconDesc']))
        assert re.search(r'[0-9]\d*.[0-9]\d*', str(res.json()['data']['book']['bookScore']))
        assert re.search(r'\d+', str(res.json()['data']['book']['iconType']))
        assert re.search(r'\d+', str(res.json()['data']['book']['lastChapterId']))
        assert re.search(r'\w+', str(res.json()['data']['book']['clickNum']))
        assert re.search(r'\w+', str(res.json()['data']['book']['introduction']))
        assert re.search(r'\w+', str(res.json()['data']['book']['disclaimer']))
        assert re.search(r'\d', str(res.json()['data']['book']['status']))
        assert re.search(r'\w+', str(res.json()['data']['chapterName']))
        assert re.search(r'\d', str(res.json()['data']['isLowerShelf']))
