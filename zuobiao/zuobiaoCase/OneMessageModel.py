# coding:utf-8
# 消息一对一给红鲤鱼发送消息及语音
#test1：发送文字消息及语音消息
#test2：发送语音消息松开试听
#test3:发送语音消息松开试听取消
# test4:发送语音然后左划删除
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from Utills.GetAppiumHelp import GetAppiumHelp

import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class OneMessageModel(unittest.TestCase):
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

    # 发送消息及语音
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
        time.sleep(1)
        MessagePage().Chat_Message().send_keys("哈哈哈哈哈哈   啦啦啦啦啦了")
        time.sleep(1)
        # 点击发送
        MessagePage().Chat_Send().click()
        time.sleep(1)
        MessagePage().Chat_Message().send_keys("跑不通了怎么办")
        time.sleep(2)
        MessagePage().Chat_Send().click()
        time.sleep(1)
        MessagePage().Chat_Message().send_keys("马上就要爆红了")
        time.sleep(2)
        MessagePage().Chat_Send().click()
        time.sleep(1)
        # 点击语音按钮
        MessagePage().Chat_Voice().click()
        time.sleep(1)
        # 长按发语音
        GetAppiumHelp().voice()
        time.sleep(3)

    # 发送语音消息松开试听发送
    def test_2(self):
        self.driver.swipe(540, 1524, 150, 1548, 25000)
        # 点击试听播放按钮
        MessagePage().shiting().click()
        #点击发送试听
        MessagePage().shifasong().click()

    #发送语音消息松开试听取消
    def test_3(self):

        self.driver.swipe(540,1524,150,1548,25000)
        #点击取消
        MessagePage().shiquxiao().click()
        time.sleep(1)

    #发送语音然后左划删除
    def test_4(self):
        self.driver.swipe(540,1524,923,1531,25000)


if __name__ == "__main__":
    unittest.main()
