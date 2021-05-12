import requests
import pytest


class TestCase:

    def test_get_code(self):
        url = 'http://95.kky.dzods.cn/glory/fastapp/2102?ver=5502450&appVer=5.5.2.450'
        header = {'utdidTmp': 'tmp_1615874327600AxgpeLJzHR',
                   'osvc': '29',
                   'scw': '1080',
                   'utdid': '8a295e1f0dcd475ac18c05ebc30683f3',
                   'pname': 'com.dianzhong.xgmfxs',
                   'osvn': '10',
                   'channelCodeFee': 'KYY1000004',
                   'triggerTime': '20210316135847',
                   'userId': '2036595',
                   'readPref': '1',
                   'scDistinctId': '1615874327537-6147661-0d109e5b509c3-2619848',
                   't': 'pgDY3DZ1LH0UBviswPJ2+Q==',
                   'pfvc': '1078',
                   'domain': '3',
                   'sch': '2110',
                   'model': 'YAL-AL10',
                   'pfvn': '1.078',
                   'Accept-Language': 'zh-CN',
                   'brand': 'HONOR',
                   'channelCode': 'KYY1000004',
                   'user-agent': 'Mozilla/5.0 (Linux; Android 10; YAL-AL10 Build/HUAWEIYAL-AL10;)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/18.0.1025 Mobile Safari/537.36 hap/1078/huawei com.huawei.fastapp/3.1.2.311 com.dianzhong.xgmfxs/5.5.2.450 ({"packageName":"com.nearme.instant.platform","type":"unknown","extra":{}})',
                   'Content-Type': 'text/plain',
                   'charset': 'utf-8',
                   'Content-Length': '2',
                   'Host': '95.kky.dzods.cn',
                   'Accept-Encoding': 'gzip',
                   'Connection': 'keep-alive'}
        params = {
            "appName": "点众阅读",
            'phoneNum': '15700000000'
        }
        res = requests.post(url, headers=header, json=params)
        print(res.status_code)
        print(res.json())


    # @pytest.mark.order(1)
    def test_get_token(self):
        url = 'http://95.kky.dzods.cn/glory/fastapp/2105?ver=5502450&appVer=5.5.2.450'
        header = {'utdidTmp': 'tmp_1615874327600AxgpeLJzHR',
                   'osvc': '29',
                   'scw': '1080',
                   'utdid': '8a295e1f0dcd475ac18c05ebc30683f3',
                   'pname': 'com.dianzhong.xgmfxs',
                   'osvn': '10',
                   'channelCodeFee': 'KYY1000004',
                   'triggerTime': '20210316135847',
                   'userId': '2036595',
                   'readPref': '1',
                   'scDistinctId': '1615874327537-6147661-0d109e5b509c3-2619848',
                   't': 'pgDY3DZ1LH0UBviswPJ2+Q==',
                   'pfvc': '1078',
                   'domain': '3',
                   'sch': '2110',
                   'model': 'YAL-AL10',
                   'pfvn': '1.078',
                   'Accept-Language': 'zh-CN',
                   'brand': 'HONOR',
                   'channelCode': 'KYY1000004',
                   'user-agent': 'Mozilla/5.0 (Linux; Android 10; YAL-AL10 Build/HUAWEIYAL-AL10;)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/18.0.1025 Mobile Safari/537.36 hap/1078/huawei com.huawei.fastapp/3.1.2.311 com.dianzhong.xgmfxs/5.5.2.450 ({"packageName":"com.nearme.instant.platform","type":"unknown","extra":{}})',
                   'Content-Type': 'text/plain',
                   'charset': 'utf-8',
                   'Content-Length': '2',
                   'Host': '95.kky.dzods.cn',
                   'Accept-Encoding': 'gzip',
                   'Connection': 'keep-alive'}
        params = {
            'validCode': '1234',
            'bindId': '15700000000',
            'accountType': 1,
            'type': 1
        }
        res = requests.post(url, headers=header, json=params)
        print(res.status_code)
        print(res.json())
        # print(res.json()['data']['operList'][0]['id'])
        # print(res.json()['data']['operList'][0]['operationInfo']['id'])
        # print(res.json()['data']['operList'][0]['actUrl'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        # assert res.json()['data']['operList'][0]['id'] == 378
