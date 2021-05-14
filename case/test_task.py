from basecase.basecase import BaseCase


class TestTask(BaseCase):
    def test_task(self):
        res = self.task.task()
        print(res.json())
        print('requestId：' + res.headers['requestId'])
        assert res.status_code == 200
