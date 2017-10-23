#-*-coding；utf-8-*-
import unittest,time
from Utills.GetAppiumDriver import GetAppiumDriver
import unittest,time
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.picture import Picture
from CommonFunction.Miliao_Page import Miliao_Page
from CommonFunction.Face import Face

#test1:点击红鲤鱼进行密聊发照片
#test:2发送密聊文本信息
#test:3发送表情
#test:4全局搜索密聊


class Miliao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDriver().driver

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver = GetAppiumDriver().driver
        cls.driver.quit()

    # test1：点击红鲤鱼进行密聊发照片
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
        # 点击回到消息页面
        MessagePage().Message().click()
        time.sleep(2)
        # 点击联系人
        ContactPage().Contact().click()
        time.sleep(4)
        # 点击我的好友分组
        ContactPage().Myfriend().click()
        time.sleep(2)
        # 选择我的好友分组里的好友
        ContactPage().Friend().click()
        time.sleep(2)
        # 点击红鲤鱼资料详情页发送消息
        MessagePage().SendMessage().click()
        time.sleep(2)
        #点击加号
        Miliao_Page().Jiahao_Miliao().click()
        time.sleep(1)
        #点击密聊
        Miliao_Page().Miliao().click()
        time.sleep(2)
        # 点击相册
        Picture().tupian().click()
        time.sleep(1)
        # 选择照片发送
        self.driver.tap([(649, 297)])
        time.sleep(1)
        self.driver.tap([(978, 299)])
        time.sleep(1)
        self.driver.tap([(290, 683)])
        time.sleep(1)
        # 点击发送按钮
        Picture().fasong().click()
        time.sleep(4)

    #test:2发送文本信息
    def test_2(self):
        #点击输入框
        Miliao_Page().Miliao_Shurukuang().send_keys('测试密聊')
        time.sleep(1)
        #发送
        Miliao_Page().Miliao_Fasong().click()
        time.sleep(2)

    #test:3发送表情
    def test_3(self):
        Face().biaoqing().click()
        time.sleep(1)
        self.driver.tap([(390, 1392)])
        time.sleep(1)
        self.driver.swipe(862, 1450, 141, 1467)
        time.sleep(1)
        self.driver.tap([(689, 1685)])
        self.driver.swipe(862, 1450, 141, 1467)
        time.sleep(1)
        self.driver.tap([(558, 1266)])
        time.sleep(1)
        # 点击发送
        MessagePage().Chat_Send().click()
        time.sleep(2)

    # test:4全局搜索密聊
    def test_4(self):
        #点击返回
        Miliao_Page().Back().click()
        time.sleep(1)
        #点击返回
        Miliao_Page().Back().click()
        time.sleep(1)
        #点击放大镜搜索、
        Miliao_Page().Fangdajing_Sousu().click()
        time.sleep(1)
        #点击搜索
        Miliao_Page().Fangdajing_Shurukuang().click()
        time.sleep(1)
        # 在搜索框中搜索红鲤鱼
        Miliao_Page().Fangdajing_Zhensrk().send_keys('红鲤鱼')
        time.sleep(3)
        #点击红鲤鱼查看密聊
        ContactPage().Friend().click()
        time.sleep(3)
        #点击返回，
        Miliao_Page().Back().click()
        time.sleep(1)
        #点击取消
        Miliao_Page().Fangdajing_Quxiao().click()
        time.sleep(1)
        Miliao_Page().Fangdajing_Quxiao().click()
        time.sleep(1)

if __name__=="__main__":
    unittest.main()





