from api.bookdetails import BookDetails
from api.getcode import GetCode
from api.login import LogIn
from api.logout import LogOut
from api.olduserlogin import OldUserLogin
from api.updateuserinfo import UpdateUserInfo
from api.userauthorize import UserAuthorize
from api.usercenter import UserCenter


class BaseCase:
    def setup(self):
        # 实例化接口,供case层使用
        self.getcode = GetCode()
        self.login = LogIn()
        self.logout = LogOut()
        self.olduserlogin = OldUserLogin()
        self.updateuserinfo = UpdateUserInfo()
        self.userauthorize = UserAuthorize()
        self.usercenter = UserCenter()
        self.bookdetails = BookDetails()
