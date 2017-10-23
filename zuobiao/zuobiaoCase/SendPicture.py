#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.picture import Picture



import time
import unittest
#test1:正常发送三张照片
#test2：预览后发送照片
import sys,os
sys.path.append(os.getcwd())
class SendPicture(unittest.TestCase):
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
    #发送3张照片
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
        #点击红鲤鱼资料详情页
        MessagePage().SendMessage().click()
        time.sleep(1)
        #点击相册
        Picture().tupian().click()
        time.sleep(1)
        #选择照片发送
        self.driver.tap([(649,297)])
        time.sleep(1)
        self.driver.tap([(978,299)])
        time.sleep(1)
        self.driver.tap([(290,683)])
        time.sleep(1)
        #点击发送按钮
        Picture().fasong().click()
        time.sleep(4)


    #选择后预览发送
    def test_2(self):
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
        #点击预览
        Picture().yulan().click()
        time.sleep(1)
        #点击完成
        Picture().fasong().click()












if __name__=="__main__":
    unittest.main()