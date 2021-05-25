import re

from basecase.basecase import BaseCase


class TestLastChapter(BaseCase):
    def test_last_chapter(self):
        res = self.last_chapter.last_chapter()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\w+', res.json()['data']['recoText'])
        assert re.search(r'\d+', str(res.json()['data']['recommentList'][0]['rankBookVo']['classifyId']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['rankBookVo']['rankName']))
        assert re.search(r'\d', str(res.json()['data']['recommentList'][0]['rankBookVo']['classifyType']))
        assert re.search(r'\d+', str(res.json()['data']['recommentList'][0]['rankBookVo']['sort']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['rankBookVo']['classifyName']))
        assert re.search(r'\d+', str(res.json()['data']['recommentList'][0]['rankBookVo']['bookId']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['threeTypeName']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['modelId']))
        assert re.search(r'http://\w+', str(res.json()['data']['recommentList'][0]['coverWap']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['twoTypeName']))
        assert re.search(r'\d', str(res.json()['data']['recommentList'][0]['draw']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['bookName']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['content']))
        assert re.search(r'\d+', str(res.json()['data']['recommentList'][0]['bookId']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['clickNum']))
        assert re.search(r'\d+', str(res.json()['data']['recommentList'][0]['logId']))
        assert re.search(r'\d+', str(res.json()['data']['recommentList'][0]['nextChapterId']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['introduction']))
        assert re.search(r'\w+', str(res.json()['data']['recommentList'][0]['recId']))
        assert re.search(r'\d', str(res.json()['data']['type']))
        assert re.search(r'\d', str(res.json()['data']['status']))
        assert re.search(r'\d+', str(res.json()['data']['userTacticsVo']['sourceId']))
        assert re.search(r'\d+', str(res.json()['data']['userTacticsVo']['tacticsId']))
        assert re.search(r'\d', str(res.json()['data']['userTacticsVo']['isDot']))
        assert re.search(r'\w+', str(res.json()['data']['userTacticsVo']['sourceName']))
        assert re.search(r'\w+', str(res.json()['data']['userTacticsVo']['tacticsName']))
        assert re.search(r'\d', str(res.json()['data']['bookStyle']))

