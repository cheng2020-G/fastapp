from api.adddesktop import AddDesktop
from api.appstart import AppStart
from api.appstartapi import AppStartApi
from api.bookdetails import BookDetails
from api.bookhome import BookHome
from api.category import CateGory
from api.categoryseconf import CateGorySecond
from api.chapter import Chapter
from api.chapterpay import ChapterPay
from api.collectcards import CollectCards
from api.coupon import Coupon
from api.feedback import FeedBack
from api.free import Free
from api.freesecond import FreeSecond
from api.fronterror import FrontError
from api.get_coupon import GetCoupon
from api.get_manjianactivity import GetManJianActivity
from api.getcode import GetCode
from api.getcollectcards import GetCollectCards
from api.gettruntableactivity import GetTruntableActivity
from api.lastchapter import LastChapter
from api.localpush import LocalPush
from api.login import LogIn
from api.logout import LogOut
from api.look import Look
from api.lottery import Lottery
from api.manjianactivity import ManJianActivity
from api.morerechargeactivity import MoreRechargeActivity
from api.olduserlogin import OldUserLogin
from api.order import Order
from api.orderinform import OrderInform
from api.playup import PlayUp
from api.position import Position
from api.prestrain import PresTrain
from api.push import Push
from api.rank import Rank
from api.readbegin import ReadBegin
from api.readhold import ReadHold
from api.readtime import ReadTime
from api.rechargeactivity import RechargeActivity
from api.rechargelist import RechargeList
from api.rechargerecord import RechargeRecord
from api.recommendedbooks import RecommendedBooks
from api.search import Search
from api.searchthink import SearchThink
from api.sendbook import SendBook
from api.sharecount import ShareCount
from api.shelfclouds import ShelfClouds
from api.sign import Sign
from api.signin import SignIn
from api.spendlist import SpendList
from api.task import Task
from api.turntableactivity import TurntableActivity
from api.updateuserinfo import UpdateUserInfo
from api.userauthorize import UserAuthorize
from api.usercenter import UserCenter
from api.usercoupon import UserCoupon
from api.vipactivity import VipActivity


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
        self.fronterror = FrontError()
        self.localpush = LocalPush()
        self.coupon = Coupon()
        self.getcoupon = GetCoupon()
        self.usercoupon = UserCoupon()
        self.position = Position()
        self.rechargeactivity = RechargeActivity()
        self.sign = Sign()
        self.signin = SignIn()
        self.vipactivity = VipActivity()
        self.sharecount = ShareCount()
        self.turntableactivity = TurntableActivity()
        self.getturntableactivity = GetTruntableActivity()
        self.lottery = Lottery()
        self.manjianactivity = ManJianActivity()
        self.getmanjianactivity = GetManJianActivity()
        self.morerechargeactivity = MoreRechargeActivity()
        self.collectcards = CollectCards()
        self.getcollectcards = GetCollectCards()
        self.look = Look()
        self.playup = PlayUp()
        self.search = Search()
        self.searchthink = SearchThink()
