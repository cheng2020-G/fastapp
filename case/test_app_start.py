import re

from basecase.basecase import BaseCase


class TestAppStart(BaseCase):
    def test_app_start(self):
        res = self.app_start.app_start()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        print(res.json()['data']['tactics'])
        print(type(res.json()['data']['tactics']))
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        for i in res.json()['data']['tactics']:
            print(i)
            print(type(i))
            assert re.search(r'\d', str(i['type']))
            assert re.search(r'\d+', str(i['location']))
            # assert re.search(r'\w+', str(i['operationName']))
            assert re.search(r'\d+', str(i['userTacticsVo']['tacticsId']))
            assert re.search(r'\w+', str(i['userTacticsVo']['tacticsName']))
            assert re.search(r'\d+', str(i['userTacticsVo']['sourceId']))
            assert re.search(r'\w+', str(i['userTacticsVo']['sourceName']))
            assert re.search(r'\d', str(i['userTacticsVo']['isDot']))
            # for j in i['videoTacticsVoList']:
            #     print(j)
            #     assert re.search(r'\d', str(j['id']))
            #     assert re.search(r'\d', str(j['start']))
            #     assert re.search(r'\d', str(j['frequency']))
        assert re.search(r'\d', str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['id']))
        assert re.search(r'\d+',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['bookId']))
        assert re.search(r'\w+',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['remark']))
        assert re.search(r'http://\w+',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['address']))
        assert re.search(r'\w+',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['bookName']))
        assert re.search(r'http://\w+',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['coverWap']))
        assert re.search(r'http://\w+', str(
            res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['videoCoverWapp']))
        assert re.search(r'[0-9]\d*.[0-9]\d*',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['fraction']))
        assert re.search(r'True|False',
                         str(res.json()['data']['tactics'][0]['videoTacticsVoList'][0]['videoList'][0]['inBookShelf']))
        assert re.search(r'\d+', str(res.json()['data']['freeLimitUt']['tacticsId']))
        assert re.search(r'\w+', str(res.json()['data']['freeLimitUt']['tacticsName']))
        assert re.search(r'\d+', str(res.json()['data']['freeLimitUt']['sourceId']))
        assert re.search(r'\w+', str(res.json()['data']['freeLimitUt']['sourceName']))
        assert re.search(r'\d', str(res.json()['data']['freeLimitUt']['isDot']))

    def test_app_start_new(self):
        res = self.app_start.app_start_new()
        print('请求url' + res.url)
        print('requestId: ' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
