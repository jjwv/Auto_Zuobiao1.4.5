#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.Sum import Sum


#test1查找好友直接发送语音
#test2:#查找好友进入聊天页面发送语音
#test3:视频通话
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class SumModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=GetAppiumDriver().driver

    def setUp(self):
        pass

    def tearDown(self):
         pass


    @classmethod
    def tearDownClass(cls):
        cls.driver=GetAppiumDriver().driver
        cls.driver.quit()

    # test1查找好友进入聊天发送语音
    def test_1(self):
        time.sleep(3)
        # 点击浮层
        LoginPage().fuceng().click()
        time.sleep(2)
        #输入账号
        LoginPage().zhanghao().send_keys("13691515688")
        #输入密码
        time.sleep(3)
        LoginPage().password().send_keys("123456")
        #点击登录
        time.sleep(2)
        LoginPage().login_btn().click()
        time.sleep(5)
        #点击关闭新手指导
        LoginPage().close_xin().click()
        time.sleep(2)
        #点击到我的进去我的页面
        MyPage().MyBtn().click()

        #获取title
        a=MyPage().text1().text
        if a=="榴莲牛奶流沙包":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")
        #点击回到消息页面
        MessagePage().Message().click()
        time.sleep(2)
        #点击联系人
        ContactPage().Contact().click()
        time.sleep(4)
        #点击我的好友分组
        ContactPage().Myfriend().click()
        time.sleep(2)
        #选择我的好友分组里的好友
        ContactPage().Friend().click()
        time.sleep(2)
        #点击语音呼叫
        MessagePage().SendVoice().click()
        time.sleep(4)
        # 点击取消
        Sum().Quxiao().click()


     #视频通话
    def test_2(self):
        # 点击红鲤鱼资料详情页发送消息
        MessagePage().SendMessage().click()
        time.sleep(1)
        # 点击加号
        Sum().jiahao().click()
        time.sleep(1)
        # 点击语音通话
        #Sum().Yunyin().click()
        self.driver.tap([(140,1372)])
        time.sleep(3)
        # 点击免提
        Sum().Mianti().click()
        time.sleep(3)
        # 点击静音
        Sum().Jingyin().click()
        time.sleep(5)
        # 点击取消
        Sum().Quxiao().click()
        time.sleep(1)

    #test3: 视频通话
    def test_3(self):
        # 点击加号
        Sum().jiahao().click()
        # 点击视频通话
        Sum().Shipin().click()
        # 点击免提
        Sum().Mianti().click()
        time.sleep(3)
        # 点击静音
        Sum().Jingyin().click()
        time.sleep(5)
        # 点击取消
        Sum().Quxiao().click()


if __name__=="__main__":
    unittest.main()