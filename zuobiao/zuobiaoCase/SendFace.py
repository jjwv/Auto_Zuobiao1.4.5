#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.Face import Face




#test1发送表情
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class SendFace(unittest.TestCase):
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
        time.sleep(3)
        LoginPage().login_btn().click()
        time.sleep(4)
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
        #点击红鲤鱼资料详情页发送消息
        MessagePage().SendMessage().click()
        time.sleep(1)
        Face().biaoqing().click()
        time.sleep(1)
        self.driver.tap([(390,1392)])
        time.sleep(1)
        self.driver.swipe(862,1450,141,1467)
        time.sleep(1)
        self.driver.tap([(689,1685)])
        self.driver.swipe(862,1450,141,1467)
        time.sleep(1)
        self.driver.tap([(558,1266)])
        time.sleep(1)
        #点击发送
        MessagePage().Chat_Send().click()
        time.sleep(2)




if __name__=="__main__":
    unittest.main()
