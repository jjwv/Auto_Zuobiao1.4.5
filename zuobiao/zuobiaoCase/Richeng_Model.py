#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.Richeng_Page import Richeng_Page
from Utills.GetAppiumHelp import GetAppiumHelp

#test1：创建日程
#test2:创建多个日程，有提醒
#test3：取消日程
#test4:删除日程
#test5:搜索日程
#test6:下滑选择当天以前的日期创建日程
#test7:选择跨月份的日期创建日程
#test8:
#test9:
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class Richeng_Model(unittest.TestCase):
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

    # test1：创建日程
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
        #点击日程
        Richeng_Page().Richeng().click()
        time.sleep(2)
        #点击创建日程
        self.driver.tap([(1000,178)])
        time.sleep(1)
        #点击日程内容输入框
        Richeng_Page().Ric_Shuruk().send_keys('我也不知道该提示什么')
        time.sleep(1)
        #选择开始时间
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        self.driver.swipe(750,1790,750,1533,500)
        time.sleep(1)
        #点击完成
        Richeng_Page().Wancheng().click()
        time.sleep(1)
        #点击结束
        Richeng_Page().Jieshu().click()
        time.sleep(1)
        self.driver.swipe(970,1800,970,1670)
        time.sleep(1)
        # 点击完成
        Richeng_Page().Wancheng().click()
        time.sleep(1)
        #点击提醒
        Richeng_Page().Tixing().click()
        time.sleep(1)
        self.driver.swipe(500,1800,500,1660,500)
        #点击总完成
        Richeng_Page().Right().click()
        time.sleep(2)
        #回到日程页面
        Richeng_Page().Back().click()
        time.sleep(1)


    #test2:创建多个日程，有提醒
    def test_2(self):
        # 点击创建日程
        self.driver.tap([(1000, 178)])
        time.sleep(2)
        # 点击日程内容输入框
        Richeng_Page().Ric_Shuruk().send_keys('下午开会 地点金源大厦')
        time.sleep(1)
        # 选择开始时间
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        self.driver.swipe(750, 1790, 750, 1533, 500)
        time.sleep(1)
        # 点击完成
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        # 点击结束
        Richeng_Page().Jieshu().click()
        time.sleep(1)
        self.driver.swipe(970, 1800, 970, 1670)
        time.sleep(1)
        # 点击提醒
        Richeng_Page().Tixing().click()
        time.sleep(1)
        self.driver.swipe(500, 1800, 500, 1660, 500)
        # 点击完成
        Richeng_Page().Right().click()
        time.sleep(3)

    # test3：取消日程
    def test_3(self):
        #点击取消的小方框
        Richeng_Page().Qx_Fangkuang().click()
        time.sleep(1)

    # test4:删除日程
    def test_4(self):
        #点击第一个日程
        self.driver.tap([(440,608)])
        time.sleep(1)
        #点击编辑
        Richeng_Page().Right().click()
        time.sleep(1)
        #点击删除日程
        Richeng_Page().Shanchuricheng().click()
        time.sleep(1)
        #点击弹窗中的删除
        Richeng_Page().Tanchuang_Shanchu().click()
        time.sleep(2)

    # test5:搜索日程
    def test_5(self):
        #点击放大镜
        self.driver.tap([(845,170)])
        time.sleep(1)
        #在搜索输入框中输入地点
        Richeng_Page().Sousu_Shurukuang().send_keys('地点')
        time.sleep(1)
        #点击一搜索的输入框
        self.driver.tap([(425,330)])
        time.sleep(1)
        #点击返回
        Richeng_Page().Back().click()
        time.sleep(1)
        #搜索页面点击取消
        Richeng_Page().Sousu_Quxiao().click()
        time.sleep(1)

    # test6:下滑选择当天以前的日期创建日程
    def test_6(self):
        #下滑
        GetAppiumHelp().UpToDown()
        time.sleep(1)
        #向右划，到前一个月
        GetAppiumHelp().LeftToRight()
        time.sleep(1)
        #创建日程
        # 点击创建日程
        self.driver.tap([(1000, 178)])
        time.sleep(2)
        # 点击日程内容输入框
        Richeng_Page().Ric_Shuruk().send_keys('哈哈哈哈一会开会 地点北苑大酒店')
        time.sleep(1)
        # 选择开始时间
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        self.driver.swipe(750, 1790, 750, 1533, 500)
        time.sleep(1)
        # 点击完成
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        # 点击结束
        Richeng_Page().Jieshu().click()
        time.sleep(1)
        self.driver.swipe(970, 1800, 970, 1670)
        time.sleep(1)
        # 点击提醒
        Richeng_Page().Tixing().click()
        time.sleep(1)
        self.driver.swipe(500, 1800, 500, 1660, 500)
        # 点击完成
        Richeng_Page().Right().click()
        time.sleep(3)

    # test7:选择跨月份的日期创建日程
    def test_7(self):
        #向左滑屏
        GetAppiumHelp().RightToLeft()
        time.sleep(1)
        # 向左滑屏
        GetAppiumHelp().RightToLeft()
        time.sleep(1)
        #创建日程
        # 点击创建日程
        self.driver.tap([(1000, 178)])
        time.sleep(2)
        # 点击日程内容输入框
        Richeng_Page().Ric_Shuruk().send_keys('哈哈哈哈一会开会 地点北苑大酒店')
        time.sleep(1)
        # 选择开始时间
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        self.driver.swipe(750, 1790, 750, 1533, 500)
        time.sleep(1)
        # 点击完成
        Richeng_Page().Kaishi().click()
        time.sleep(1)
        # 点击结束
        Richeng_Page().Jieshu().click()
        time.sleep(1)
        self.driver.swipe(970, 1800, 970, 1670)
        time.sleep(1)
        # 点击提醒
        Richeng_Page().Tixing().click()
        time.sleep(1)
        self.driver.swipe(500, 1800, 500, 1660, 500)
        # 点击完成
        Richeng_Page().Right().click()
        time.sleep(3)






















