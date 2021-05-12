from api.getuserId import GetUserId
from api.gettoken import Token


class BaseCase:
    def setup(self):
        # 实例化接口,供case层使用
        self.user_id = GetUserId()
        self.token = Token()
