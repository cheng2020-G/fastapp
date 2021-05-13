from api.bookdetails import BookDetails
from api.chapter import Chapter
from api.getcode import GetCode
from api.lastchapter import LastChapter
from api.login import LogIn
from api.logout import LogOut
from api.olduserlogin import OldUserLogin
from api.recommendedbooks import RecommendedBooks
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
        self.chapter = Chapter()
        self.lastchapter = LastChapter()
        self.recommendedbooks = RecommendedBooks()
