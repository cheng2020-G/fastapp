import re

import jsonpath as jsonpath
import json
from basecase.basecase import BaseCase


class TestShelfClouds(BaseCase):
    def test_shelf_clouds(self):
        res = self.shelf_clouds.shelf_clouds()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        # assert jsonpath.jsonpath(res.json(), '$.retCode') == 0
        # print(jsonpath.jsonpath(res.json(), '$.retCode'))
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert re.search(r'\d+', str(res.json()['data']['size']))
        assert re.search(r'\d+', str(res.json()['data']['bookSize']))
        assert re.search(r'\d+', res.json()['data']['content'][0]['uid'])
        assert re.search(r'\d+', str(res.json()['data']['content'][0]['bookId']))
        assert re.search(r'\d+', str(res.json()['data']['content'][0]['utime']))
        assert re.search(r'\d+', str(res.json()['data']['content'][0]['chapterId']))
        assert re.search(r'\S+', res.json()['data']['content'][0]['author'])
        assert re.search(r'http://\S+', res.json()['data']['content'][0]['coverImage'])
        assert re.search(r'\S+', res.json()['data']['content'][0]['status'])
        assert re.search(r'\d', str(res.json()['data']['content'][0]['mstatus']))
        assert re.search(r'\S+', res.json()['data']['content'][0]['cname'])
        assert re.search(r'\d', str(res.json()['data']['content'][0]['isUpdate']))
        assert re.search(r'\d', str(res.json()['data']['content'][0]['cindex']))
        assert re.search(r'\d', str(res.json()['data']['content'][0]['iconType']))
        assert re.search(r'\S+', res.json()['data']['content'][0]['iconDesc'])
        # assert re.search(r'\S+', res.json()['data']['content'][0]['omap']['channel_name'])
        # assert re.search(r'\d+', str(res.json()['data']['content'][0]['omap']['column_id']))
        # assert re.search(r'\d+', str(res.json()['data']['content'][0]['omap']['trigger_time']))
        # assert re.search(r'\d+', str(res.json()['data']['content'][0]['omap']['channel_pos']))
        # assert re.search(r'\d+', str(res.json()['data']['content'][0]['omap']['content_type']))
        # assert re.search(r'\d+', str(res.json()['data']['content'][0]['omap']['content_id']))
        # assert re.search(r'\S+', res.json()['data']['content'][0]['omap']['origin'])
        # assert re.search(r'\S+', res.json()['data']['content'][0]['omap']['column_name'])
        # assert re.search(r'\d+', str(json(res.json()['data']['content'][0]['omap']['action'])))
