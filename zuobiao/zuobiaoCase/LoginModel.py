#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.SettingPage import SettingPage


import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class LoginModel(unittest.TestCase):
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

    def test_login(self):
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

        print("2")
        #获取title
        a=MyPage().text1().text
        if a=="榴莲牛奶流沙包":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")
    #邮箱登录
    def test_email(self):
        time.sleep(2)
        #点击设置按钮
        MyPage().setting().click()
        time.sleep(1)
        #点击退出登录
        SettingPage().quit().click()
        time.sleep(1)
        #点击确定按钮
        SettingPage().fuceng_quie().click()
        time.sleep(3)
        #清除上次登录账号
        LoginPage().zhanghao().clear()
        time.sleep(1)
        #输入邮箱账号
        LoginPage().zhanghao().send_keys("cuiwenhaozing@163.com")
        time.sleep(1)
        #输入密码
        LoginPage().password().send_keys("123456")
        #点击登录
        LoginPage().login_btn().click()
        #点击进入我的页面
        MyPage().MyBtn().click()
        #获取邮箱title
        b=MyPage().text1().text
        if b=="红鲤鱼与绿鲤鱼与驴":
            print("邮箱登陆成功")
        else:
            print("邮箱登录失败")



if __name__=="__main__":
    unittest.main()







