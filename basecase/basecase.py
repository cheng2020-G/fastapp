from api.getcode import GetCode
from api.login import LogIn



class BaseCase:
    def setup(self):
        # 实例化接口,供case层使用
        self.getcode = GetCode()
        self.login = LogIn()

