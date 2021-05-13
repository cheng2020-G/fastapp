import yaml

from base.baseapi import BaseApi


class Task(BaseApi):
    def task(self):
        data = yaml.safe_load(open('D:/script/fastapp/data/task.yaml'))
        return self.send(data)