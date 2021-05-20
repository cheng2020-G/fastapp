import yaml

from base.baseapi import BaseApi


class GetParameters(BaseApi):

    def get_code(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/get_code.yaml'))
        res = self.http(data)
        print('请求url： ' + res.url)
        print('requestId: ' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200

    # @pytest.mark.order(1)
    def get_token(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/login.yaml'))
        res = self.http(data)
        print('请求url： ' + res.url)
        print('requestId: ' + res.headers['requestId'])
        print(res.json())
        print('token: ' + res.json()['data']['result']['token'])
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        return res.json()['data']['result']['token']


# if __name__ == '__main__':
#     GetParameters().get_code()
#     GetParameters().get_token()
