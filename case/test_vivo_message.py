import pytest

from basecase.basecase import BaseCase


class TestVivoMessage(BaseCase):
    @pytest.mark.skip
    def test_vivo_message(self):
        res = self.vivom_essage.vivo_message()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        print('templateIds: ' + res.json()['data']['templateIds'])
        assert res.status_code == 200
