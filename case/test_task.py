from basecase.basecase import BaseCase


class TestTask(BaseCase):
    def test_task(self):
        res = self.task.task()
        print(res.json())
        assert res.status_code== 200