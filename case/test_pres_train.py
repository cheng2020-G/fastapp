from basecase.basecase import BaseCase


class TestPresTrain(BaseCase):
    def test_pres_train(self):
        res = self.prestrain.prestrain()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
