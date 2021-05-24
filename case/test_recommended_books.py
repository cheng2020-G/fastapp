import re

from basecase.basecase import BaseCase


class TestRecommendBooks(BaseCase):
    def test_recommended_books(self):
        res = self.recommended_books.recommended_books()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['recId'] == 'app_rec'
        assert re.search(r'\d', str(res.json()['data']['styleType']))
        assert re.search(r'\d+', res.json()['data']['books'][0]['bookId'])
        assert re.search(r'\w+', res.json()['data']['books'][0]['bookName'])
        assert re.search(r'\w+', res.json()['data']['books'][0]['author'])
        assert re.search(r'http://\w+', res.json()['data']['books'][0]['coverWap'])
        assert re.search('.+?', res.json()['data']['books'][0]['introduction'])
        assert re.search('.+?', res.json()['data']['books'][0]['clickNum'])
        assert re.search('', res.json()['data']['books'][0]['desc'])
        assert re.search(r'\d+', str(res.json()['data']['books'][0]['iconType']))
        assert re.search(r'\S+', str(res.json()['data']['books'][0]['twoTypeName']))
        assert re.search(r'\S+', str(res.json()['data']['books'][0]['threeTypeName']))
        assert re.search(r'\d+', str(res.json()['data']['books'][0]['rankBookVo']['bookId']))
        assert re.search(r'\w+', str(res.json()['data']['books'][0]['rankBookVo']['rankName']))
        assert re.search(r'\d', str(res.json()['data']['books'][0]['rankBookVo']['classifyType']))
        assert re.search(r'\d+', str(res.json()['data']['books'][0]['rankBookVo']['classifyId']))
        assert re.search(r'\S+', str(res.json()['data']['books'][0]['rankBookVo']['classifyName']))
        assert re.search(r'\d+', str(res.json()['data']['books'][0]['rankBookVo']['sort']))
