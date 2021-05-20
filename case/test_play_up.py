from basecase.basecase import BaseCase


class TestPlayUp(BaseCase):
    def test_play_up(self):
        res = self.play_up.play_up()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
        assert res.json()['retCode'] == 0
        assert res.json()['isExpire'] == 1
        assert res.json()['data']['status'] == 'success'
