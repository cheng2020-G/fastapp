from basecase.basecase import BaseCase


class TestPresTrain(BaseCase):
    def test_pres_train(self):
        res = self.prestrain.prestrain()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
