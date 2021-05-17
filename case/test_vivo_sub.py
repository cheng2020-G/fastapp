import pytest

from basecase.basecase import BaseCase


class TestVivoSub(BaseCase):
    @pytest.mark.xfail
    def test_vivo_sub(self):
        res = self.vivosub.vivo_sub()
        print(res.json())
        print('requestId: ' + res.headers['requestId'])
        assert res.status_code == 200
