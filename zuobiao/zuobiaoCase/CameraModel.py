#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.Camera import Camera


import time
import unittest
#test1:点击长按正常发送和取消小视频
#test2:长按录制小视频后点击✘取消
#test3:点击一下进行拍照发送
#test4:点击一下进行拍照取消
#test5:点击转换前置摄像头进行录像
#test6:点击转换前置摄像头进行拍照
import sys,os
sys.path.append(os.getcwd())
#print(os.getcwd())
class CameraModel(unittest.TestCase):
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

    #点击长按正常发送和取消小视频
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
        #点击相机按钮
        Camera().xiangji().click()
        time.sleep(1)
        #长按录制
        self.driver.tap([(537,1711)],6000)
        time.sleep(1)
        #点击对勾发送小视频
        self.driver.tap([(810,1728)])
        time.sleep(1)


    #长按录制小视频后点击✘取消
    def test_2(self):
        # 点击相机按钮
        Camera().xiangji().click()
        time.sleep(1)
        # 长按
        self.driver.tap([(537, 1711)], 6000)
        time.sleep(2)
        #点击✘取消发送
        self.driver.tap([(273,1716)])
        time.sleep(2)
        #返回聊天页面
        self.driver.tap([(260,1702)])
        time.sleep(1)

    #点击一下进行拍照发送
    def test_3(self):
        # 点击相机按钮
        Camera().xiangji().click()
        time.sleep(2)
        # 点击一下拍照
        self.driver.tap([(537, 1711)])
        time.sleep(4)
        #点击对勾发送
        self.driver.tap([(810, 1728)])
        time.sleep(1)

    #点击一下进行拍照✘取消
    def test_4(self):
        # 点击相机按钮
        Camera().xiangji().click()
        time.sleep(1)
        # 点击一下拍照
        self.driver.tap([(537, 1711)])
        time.sleep(4)
        #点击✘
        self.driver.tap([(273, 1716)])
        time.sleep(1)
        # 返回聊天页面
        self.driver.tap([(223,1710)])
        time.sleep(1)

    #点击转换前置摄像头进行录像
    def test_5(self):
        # 点击相机按钮
        Camera().xiangji().click()
        time.sleep(1)
        #点击转换摄像头
        self.driver.tap([(830,1735)])
        # 长按录制
        self.driver.tap([(537, 1711)], 6000)
        time.sleep(1)
        # 点击对勾发送小视频
        self.driver.tap([(810, 1728)])
        time.sleep(1)

    #点击转换前置摄像头进行拍照
    def test_6(self):
        # 点击相机按钮
        Camera().xiangji().click()
        time.sleep(1)
        # 点击转换摄像头
        self.driver.tap([(830, 1735)])
        time.sleep(2)
        # 长按录制
        self.driver.tap([(537, 1711)])
        time.sleep(1)
        # 点击对勾发送小视频
        self.driver.tap([(810, 1728)])
        time.sleep(1)


if __name__=="__main__":
    unittest.main()