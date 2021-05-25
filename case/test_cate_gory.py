import re

from basecase.basecase import BaseCase


class TestCateGory(BaseCase):
    def test_cate_gory(self):
        res = self.cate_gory.cate_gory()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert re.search(r'http://\w+', str(res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['imgUrl']))
        assert re.search(r'\w+', res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['markColor'])
        assert re.search(r'\w+', res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['markMsg'])
        assert re.search(r'\w+', res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['title'])
        assert re.search(r'\d+', str(res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['cid']))
        assert re.search(r'\d+', res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['categoryMark'][0]['markId'])
        assert re.search(r'\w+', res.json()['data']['typeOneVoList'][0]['typeTwoVos'][0]['categoryMark'][0]['title'])
        assert re.search(r'\w+', res.json()['data']['typeOneVoList'][0]['categoryName'])
        assert re.search(r'\d', str(res.json()['data']['typeOneVoList'][0]['categoryId']))
        assert re.search(r'\d', str(res.json()['data']['statusMark'][0]['markId']))
        assert re.search(r'\w+', res.json()['data']['statusMark'][0]['title'])
