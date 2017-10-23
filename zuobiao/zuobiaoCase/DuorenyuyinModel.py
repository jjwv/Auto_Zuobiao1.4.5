#codingutf-8
import unittest,time
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from Utills.GetAppiumHelp import GetAppiumHelp
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.Duorenyy_Page import Duorenyy_Page

#test1：创建多人语音
#test2:多人语音界面按键操作
#test3：添加8人创建多人语音
#test4:创建多人语音然后逐渐添加用户


class Duorenyuyin_Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=GetAppiumDriver().driver

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver = GetAppiumDriver().driver
        cls.driver.quit()

    #test1：创建多人语音
    def test_1(self):
        time.sleep(3)
        # 点击浮层
        LoginPage().fuceng().click()
        time.sleep(2)
        # 输入账号
        LoginPage().zhanghao().send_keys("13691515688")
        # 输入密码
        time.sleep(3)
        LoginPage().password().send_keys("123456")
        # 点击登录
        time.sleep(3)
        LoginPage().login_btn().click()
        time.sleep(4)
        # 点击关闭新手指导
        LoginPage().close_xin().click()
        time.sleep(2)
        # 点击到我的进去我的页面
        MyPage().MyBtn().click()
        # 获取title
        a = MyPage().text1().text
        if a == "榴莲牛奶流沙包":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")
        #点击回到消息页面
        MessagePage().Message().click()
        time.sleep(2)
        # 点击联系人
        ContactPage().Contact().click()
        time.sleep(2)

        time.sleep(1)
        # 右划到群
        GetAppiumHelp().RightToLeft()
        time.sleep(2)
        GetAppiumHelp().UpToDown()
        time.sleep(2)
        # 点击鬼拉拉群  自己是群主
        #self.driver.tap([(422, 683)])
        Duorenyy_Page().Guilala().click()
        time.sleep(1)
        #点击加号
        Duorenyy_Page().Quzujiahao().click()
        time.sleep(1)
        #点击语音通话
        #Duorenyy_Page().Yuyinth().click()
        self.driver.tap([(141,1380)])
        time.sleep(3)
        #选择群成员a老范
        ContactPage().LF().click()
        time.sleep(1)
        #选择群成员宫雨菲非
        ContactPage().gyff().click()
        time.sleep(1)
        #点击确定
        Duorenyy_Page().Right().click()
        time.sleep(3)

    # test2:多人语音界面按键操作
    def test_2(self):
        #点击免提
        #Duorenyy_Page().mianti().click()
        self.driver.tap([(179,1698)])
        time.sleep(1)
        #点击麦克风
        self.driver.tap([(900,1676)])
        time.sleep(1)
        #定位语音收缩按钮
        Duorenyy_Page().Shousuo().click()
        time.sleep(1)
        #点击多人语音悬浮窗
        self.driver.tap([(958,187)])
        time.sleep(1)
        #点击挂断
        Duorenyy_Page().Guaduan().click()
        time.sleep(1)

    #test3：添加8人创建多人语音
    def test_3(self):
        # 点击加号
        Duorenyy_Page().Quzujiahao().click()
        time.sleep(1)
        # 点击语音通话
        # Duorenyy_Page().Yuyinth().click()
        self.driver.tap([(141, 1380)])
        time.sleep(3)
        # 选择群成员a老范
        ContactPage().LF().click()
        time.sleep(1)
        # 选择群成员宫雨菲非
        ContactPage().gyff().click()
        time.sleep(1)
        #选择冯瑞芳
        ContactPage().frf().click()
        time.sleep(1)
        self.driver.swipe(350,1555,355,1326,1000)
        #选择开玩笑
        ContactPage().kwx().click()
        time.sleep(1)
        #滑屏
        self.driver.swipe(443,1772,415,588,1000)
        #选择lizhifei
        ContactPage().lzf().click()
        time.sleep(1)
        #选择PC张彩蝶
        ContactPage().zcd().click()
        time.sleep(1)
        #选择qj
        ContactPage().qj().click()
        time.sleep(1)
        #选择孙登岭
        ContactPage().sdl().click()
        time.sleep(1)
        # 点击确定
        Duorenyy_Page().Right().click()
        time.sleep(3)
        # 点击挂断
        Duorenyy_Page().Guaduan().click()
        time.sleep(1)

    # test4:创建多人语音然后逐渐添加用户
    def test_4(self):
        # 点击加号
        Duorenyy_Page().Quzujiahao().click()
        time.sleep(1)
        # 点击语音通话
        # Duorenyy_Page().Yuyinth().click()
        self.driver.tap([(141, 1380)])
        time.sleep(3)
        # 选择群成员a老范
        ContactPage().LF().click()
        time.sleep(1)
        # 选择群成员宫雨菲非
        ContactPage().gyff().click()
        time.sleep(1)
        # 点击确定
        Duorenyy_Page().Right().click()
        time.sleep(3)
        #点击群聊中的加号添加通话成员
        Duorenyy_Page().Duorenyy_jiahao().click()
        time.sleep(1)
        #选择冯瑞芳
        ContactPage().frf().click()
        time.sleep(1)
        #点击完成
        Duorenyy_Page().Right().click()
        time.sleep(3)
        # 点击群聊中的加号添加通话成员
        Duorenyy_Page().Duorenyy_jiahao().click()
        time.sleep(1)
        # 选择开玩笑
        self.driver.swipe(350, 1555, 355, 1326, 1000)
        ContactPage().kwx().click()
        time.sleep(1)
        # 点击完成
        Duorenyy_Page().Right().click()
        time.sleep(3)
        # 点击麦克风
        self.driver.tap([(900, 1676)])
        time.sleep(1)
        # 点击挂断
        Duorenyy_Page().Guaduan().click()
        time.sleep(1)
















