from basecase.basecase import BaseCase


class TestTask(BaseCase):
    def test_task(self):
        res = self.task.task()
        print('请求url：' + res.url)
        print('requestId：' + res.headers['requestId'])
        print(res.json())
        assert res.status_code == 200
