#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.ContactsPage import ContactPage
from Utills.GetAppiumHelp import GetAppiumHelp
from CommonFunction.Data_Xingqing import Data_Xingqing

import time
import unittest
#test1:给响雷更改备注还原备注
#test2:点击查看工作信息
#test3:点击。。。进行举报删除联系人
#test4：点击。。。举报
import sys,os
sys.path.append(os.getcwd())
class Data_XingqModel(unittest.TestCase):
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

        #print("2")
        #获取title
        a=MyPage().text1().text
        if a=="榴莲牛奶流沙包":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")

        # 点击联系人
        ContactPage().Contact().click()
        time.sleep(2)
        GetAppiumHelp().UpToDown()
        #点击我的好友分组
        ContactPage().Myfriend().click()
        time.sleep(2)
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击响雷
        ContactPage().Xianglei().click()
        time.sleep(1)
        #点击设置备注名
        self.driver.tap([(243,718)])
        #Data_Xingqing().beizhum().click()
        time.sleep(1)
        #在输入框内更改昵称为项雷123
        Data_Xingqing().Remark().send_keys("项雷123")
        time.sleep(1)
        #点击完成
        Data_Xingqing().Right().click()
        time.sleep(1)
        #点击返回
        Data_Xingqing().Back().click()
        time.sleep(1)

        #点击项雷123
        ContactPage().Xiangleione().click()
        time.sleep(1)
        # 点击设置备注名
        self.driver.tap([(243, 718)])
        time.sleep(1)
        # 在输入框内更改昵称为项雷123
        Data_Xingqing().Remark().send_keys("项雷")
        time.sleep(1)
        # 点击完成
        Data_Xingqing().Right().click()
        time.sleep(1)

    # test2:点击查看工作信息
    def test_2(self):
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击工作信息
        self.driver.tap([(519,937)])
        #Data_Xingqing().gongzuoxinx().click()
        time.sleep(1)
        #点击返回
        Data_Xingqing().Back().click()
        time.sleep(1)
        #点击描述
        Data_Xingqing().Ms().click()
        time.sleep(1)
        #在描述输入框添加描述
        Data_Xingqing().Remark().send_keys("哈哈哈哈哈哈哈，啦啦啦啦啦")
        time.sleep(1)
        #点击完成
        Data_Xingqing().Right().click()
        time.sleep(1)
    # test3:点击。。。进行举报删除联系人
    def test_3(self):
        #点击。。。
        Data_Xingqing().Right().click()
        time.sleep(1)
        #点击删除好友
        Data_Xingqing().Delete().click()
        time.sleep(1)
        #在弹窗点击取消
        Data_Xingqing().Fcqx().click()
        time.sleep(1)
    #test4：点击。。。举报
    def test_4(self):
        #点击。。
        Data_Xingqing().Right().click()
        time.sleep(1)
        #点击..中的举报
        Data_Xingqing().Jubao().click()
        time.sleep(1)
        #点击返回
        Data_Xingqing().Back().click()




if __name__=="__main__":
    unittest.main()