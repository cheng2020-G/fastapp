import yaml

from api.add_desktop import AddDesktop
from api.api import Api
from api.login import LogIn
from basecase.basecase import BaseCase


class TestAddDesktop:
    def test_add_desktop(self):
        # res = self.add_desktop.add_desktop()
        data = yaml.safe_load(open('D:/script/fastapp/data/add_desktop.yaml'))
        # res = AddDesktop().add_desktop(data)
        # res = LogIn().login(data)
        res = Api().api(data)
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['status'] == 2
