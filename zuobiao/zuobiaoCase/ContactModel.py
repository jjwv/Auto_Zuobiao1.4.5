#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.GlfzPage import GlfzPage
from CommonFunction.Chat_Xingqing import Chat_Xingqing
from CommonFunction.Choose_Group import Choose_Group


#test1:进去管理分组添加分组
#test2:把好友更换分组
#test3：删除好友分组"哈哈"

import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class ContactModel(unittest.TestCase):
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

        print("2")
        #获取title
        a=MyPage().text1().text
        if a=="榴莲牛奶流沙包":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")
        # 点击联系人
        ContactPage().Contact().click()
        time.sleep(3)
        #长按我的好友弹出管理分组
        self.driver.tap([(544,581)],1000)
        time.sleep(1)
        #点击弹窗的管理分组
        ContactPage().Glfz().click()
        time.sleep(1)
        #点击添加分组
        GlfzPage().Tjfz().click()
        time.sleep(1)
        #填入分组名称
        GlfzPage().Qsr().send_keys("哈哈哈")
        time.sleep(1)
        #点击确定
        GlfzPage().Qding().click()
        time.sleep(3)
        #点击完成
        GlfzPage().Complete().click()
        time.sleep(1)

    #test2:把好友更换分组
    def test_2(self):
        #点击我的好友分组
        ContactPage().Myfriend().click()
        time.sleep(1)
        #找到菲姐
        ContactPage().Fj().click()
        time.sleep(1)
        #点击我的好友换分组
        Chat_Xingqing().Hfz().click()
        time.sleep(1)
        #选择哈哈哈分组
        #self.driver.tap([(375,720)])
        Choose_Group().Haha().click()
        time.sleep(1)
        #点击完成
        GlfzPage().Complete().click()
        time.sleep(5)
        #点击返回
        Chat_Xingqing().Back().click()
        time.sleep(1)

    #test3：删除好友分组"哈哈"
    def test_3(self):
        # 长按我的好友弹出管理分组
        self.driver.tap([(470,600)], 1000)
        time.sleep(1)
        #点击弹窗的管理分组
        ContactPage().Glfz().click()
        time.sleep(1)
        #点击删除分组哈
        #self.driver.tap([(89,664)])
        Choose_Group().shanchuhaha().click()
        time.sleep(1)
        #点击 删除分组
        GlfzPage().Delete_Group().click()
        time.sleep(1)
        #点击完成
        GlfzPage().Complete().click()
        time.sleep(2)
















if __name__=="__main__":
    unittest.main()