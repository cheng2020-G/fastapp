from api.adddesktop import AddDesktop
from api.appstart import AppStart
from api.appstartapi import AppStartApi
from api.bookdetails import BookDetails
from api.bookhome import BookHome
from api.category import CateGory
from api.categoryseconf import CateGorySecond
from api.chapter import Chapter
from api.chapterpay import ChapterPay
from api.feedback import FeedBack
from api.free import Free
from api.freesecond import FreeSecond
from api.getcode import GetCode
from api.lastchapter import LastChapter
from api.login import LogIn
from api.logout import LogOut
from api.olduserlogin import OldUserLogin
from api.order import Order
from api.orderinform import OrderInform
from api.prestrain import PresTrain
from api.push import Push
from api.rank import Rank
from api.readbegin import ReadBegin
from api.readhold import ReadHold
from api.readtime import ReadTime
from api.rechargelist import RechargeList
from api.rechargerecord import RechargeRecord
from api.recommendedbooks import RecommendedBooks
from api.sendbook import SendBook
from api.shelfclouds import ShelfClouds
from api.spendlist import SpendList
from api.task import Task
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
        self.sendbook = SendBook()
        self.shelfclouds = ShelfClouds()
        self.rechargelist = RechargeList()
        self.order = Order()
        self.orderinform = OrderInform()
        self.rechargerecord = RechargeRecord()
        self.spendlist = SpendList()
        self.adddesktop = AddDesktop()
        self.readtime = ReadTime()
        self.task = Task()
        self.readbegin = ReadBegin()
        self.chapterpay = ChapterPay()
        self.prestrain = PresTrain()
        self.readhold = ReadHold()
        self.appstart = AppStart()
        self.bookhome = BookHome()
        self.category = CateGory()
        self.categorysecond = CateGorySecond()
        self.free = Free()
        self.freesecond = FreeSecond()
        self.rank = Rank()
        self.push = Push()
        self.feedback = FeedBack()
        self.appstartapi = AppStartApi()
