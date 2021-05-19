from api.add_desktop import AddDesktop
from api.app_start import AppStart
from api.app_start_api import AppStartApi
from api.book_details import BookDetails
from api.book_home import BookHome
from api.cate_gory import CateGory
from api.cate_gory_second import CateGorySecond
from api.chapter import Chapter
from api.chapter_pay import ChapterPay
from api.collect_cards import CollectCards
from api.coupon import Coupon
from api.feedback import FeedBack
from api.free import Free
from api.free_second import FreeSecond
from api.front_error import FrontError
from api.get_coupon import GetCoupon
from api.get_manjian_activity import GetManJianActivity
from api.get_code import GetCode
from api.get_collect_cards import GetCollectCards
from api.get_truntable_activity import GetTruntableActivity
from api.last_chapter import LastChapter
from api.local_push import LocalPush
from api.login import LogIn
from api.logout import LogOut
from api.look import Look
from api.lottery import Lottery
from api.manjian_activity import ManJianActivity
from api.more_recharge_activity import MoreRechargeActivity
from api.old_user_login import OldUserLogin
from api.order import Order
from api.order_inform import OrderInform
from api.play_up import PlayUp
from api.position import Position
from api.prestrain import PresTrain
from api.push import Push
from api.rank import Rank
from api.read_begin import ReadBegin
from api.read_hold import ReadHold
from api.read_time import ReadTime
from api.recharge_activity import RechargeActivity
from api.recharge_list import RechargeList
from api.recharge_record import RechargeRecord
from api.recommended_books import RecommendedBooks
from api.search import Search
from api.search_keywords import SearchKeyWords
from api.search_think import SearchThink
from api.send_book import SendBook
from api.share_count import ShareCount
from api.shelf_clouds import ShelfClouds
from api.sign import Sign
from api.sign_in import SignIn
from api.spend_list import SpendList
from api.task import Task
from api.turntable_activity import TurntableActivity
from api.update_user_info import UpdateUserInfo
from api.user_system import UserSystem
from api.user_authorize import UserAuthorize
from api.user_center import UserCenter
from api.user_coupon import UserCoupon
from api.user_system_rule import UserSystemRule
from api.vip_activity import VipActivity
from api.vivo_message import VivoMessage
from api.vivo_sub import VivoSub


class BaseCase:
    def setup(self):
        # 实例化接口,供case层使用
        self.get_code = GetCode()
        self.login = LogIn()
        self.logout = LogOut()
        self.old_user_login = OldUserLogin()
        self.update_user_info = UpdateUserInfo()
        self.user_authorize = UserAuthorize()
        self.user_center = UserCenter()
        self.book_details = BookDetails()
        self.chapter = Chapter()
        self.last_chapter = LastChapter()
        self.recommended_books = RecommendedBooks()
        self.send_book = SendBook()
        self.shelf_clouds = ShelfClouds()
        self.recharge_list = RechargeList()
        self.order = Order()
        self.order_inform = OrderInform()
        self.recharge_record = RechargeRecord()
        self.spend_list = SpendList()
        self.add_desktop = AddDesktop()
        self.read_time = ReadTime()
        self.task = Task()
        self.read_begin = ReadBegin()
        self.chapter_pay = ChapterPay()
        self.prestrain = PresTrain()
        self.read_hold = ReadHold()
        self.app_start = AppStart()
        self.book_home = BookHome()
        self.cate_gory = CateGory()
        self.cate_gory_second = CateGorySecond()
        self.free = Free()
        self.free_second = FreeSecond()
        self.rank = Rank()
        self.push = Push()
        self.feedback = FeedBack()
        self.app_start_api = AppStartApi()
        self.front_error = FrontError()
        self.local_push = LocalPush()
        self.coupon = Coupon()
        self.get_coupon = GetCoupon()
        self.user_coupon = UserCoupon()
        self.position = Position()
        self.recharge_activity = RechargeActivity()
        self.sign = Sign()
        self.sign_in = SignIn()
        self.vip_activity = VipActivity()
        self.share_count = ShareCount()
        self.turntable_activity = TurntableActivity()
        self.get_turntable_activity = GetTruntableActivity()
        self.lottery = Lottery()
        self.manjian_activity = ManJianActivity()
        self.get_manjian_activity = GetManJianActivity()
        self.more_recharge_activity = MoreRechargeActivity()
        self.collect_cards = CollectCards()
        self.getcollect_cards = GetCollectCards()
        self.look = Look()
        self.play_up = PlayUp()
        self.search = Search()
        self.search_think = SearchThink()
        self.search_keywords = SearchKeyWords()
        self.user_system = UserSystem()
        self.user_system_rule = UserSystemRule()
        self.vivom_essage = VivoMessage()
        self.vivo_sub = VivoSub()
