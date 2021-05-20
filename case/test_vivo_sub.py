import pytest

from basecase.basecase import BaseCase


class TestVivoSub(BaseCase):
    @pytest.mark.skip
    def test_vivo_sub(self):
        res = self.vivo_sub.vivo_sub()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
