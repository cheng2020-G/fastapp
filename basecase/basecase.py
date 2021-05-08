from api.GetUserId import GetUserId
from api.GetToken import Token


class BaseCase:
    def setup(self):
        # 实例化getUserid接口
        self.GetUserId = GetUserId()
        self.GetToken = Token()
