#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.Top import Top
from CommonFunction.Chat_Xingqing import Chat_Xingqing
from Utills.GetAppiumHelp import GetAppiumHelp
from CommonFunction.ContactsPage import ContactPage

#test1：点击放大镜进行搜索框搜索
#test2:点击放大镜进行按联系人 聊天记录 文件进行搜索
#test3：点击铃铛查看验证消息
#test4:加号点击创建群组后解散
#test5：加号点添加联系人
#test6:加号点扫一扫
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class TopModel(unittest.TestCase):
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

    #test1点击放大镜进行搜索框搜索
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
       #点击放大镜进入搜索页面
        Top().Fangdajing().click()
        time.sleep(1)
        #点击搜索框
        Top().Sousu().click()
        time.sleep(1)
        #点击搜索框进去Zsousuo
        Top().Zsousu().send_keys("啦啦啦")
        time.sleep(2)
        #点击取消
        Top().Cancel().click()
        time.sleep(1)


    def test_2(self):
        #点击联系人搜索
        Top().Contact_btn().click()
        time.sleep(1)
        #在搜索框输入榴莲牛奶流沙包
        Top().Zsousu().send_keys("榴莲牛奶流沙包")
        time.sleep(1)
        #点击取消
        Top().Cancel().click()
        time.sleep(1)
        #点击聊天记录搜索
        Top().Contact_btn().click()
        time.sleep(1)
        #在搜素框输入哈哈哈
        Top().Zsousu().send_keys("哈哈哈")
        time.sleep(1)
        #点击取消
        Top().Cancel().click()
        time.sleep(1)

        #点击按文件搜索
        Top().File_btn().click()
        time.sleep(1)
        # 在搜索框输入榴莲牛奶流沙包
        Top().Zsousu().send_keys("搜那个文件好呢")
        time.sleep(2)
        # 点击取消
        Top().Cancel().click()
        time.sleep(1)
        Top().Cancel().click()
        time.sleep(2)

    #test3：点击铃铛查看验证消息
    def test_3(self):
        #点击铃铛
        Top().Notify().click()
        time.sleep(3)
        #点击小人头
        Top().Tjlxr().click()
        time.sleep(1)
        #点击搜索框
        Top().Sousu_T().click()
        time.sleep(1)
        #在搜索框内搜索榴莲牛奶流沙包
        Top().Zsousu().send_keys("榴莲牛奶流沙包")
        time.sleep(3)
        #点击取消
        Top().Cancel().click()
        time.sleep(1)

        #time.sleep(3)
        #点击返回验证消息页面
        Top().Back().click()
        time.sleep(2)
        #点击返回键
        Top().Back().click()

    #test4:加号点击创建群组
    def test_4(self):
        time.sleep(2)
        #点击加号
        #Top().Jiahao().click()
        self.driver.tap([(993,165)])
        time.sleep(1)
        #点击创建群组
        Top().Creat_group().click()
        time.sleep(1)
        GetAppiumHelp().UpToDown()
        time.sleep(4)
        #选择群成员
        Chat_Xingqing().Fjie().click()
        time.sleep(1)
        Chat_Xingqing().Gfei().click()
        time.sleep(1)
        #点击确定
        Chat_Xingqing().Right().click()
        time.sleep(6)
        # 创建群组后点击小人头进去群资料页
        #Top().Jqunzuzl().click()
        self.driver.tap([(997,160)])
        time.sleep(1)
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击退出群组
        Top().Exit_group().click()
        time.sleep(1)
        #点击解散
        #Top().Jqunzuzl().click()
        self.driver.tap([(537,1670)])
        time.sleep(2)
        #点击确定
        Top().Fcqd().click()

    #test5：加号点添加联系人
    def test_5(self):
        time.sleep(4)
        # 点击加号
        #Top().Jiahao().click()
        self.driver.tap([(993, 165)])
        time.sleep(1)
        #点击添加联系人
        Top().Add_friend().click()
        time.sleep(1)
        #点击添加联系人页中搜索框
        Top().Tjiasou().click()
        #在搜索框内搜索红鲤鱼
        Top().Zsousu().send_keys("红鲤鱼")
        time.sleep(2)
        #点击红鲤鱼
        Top().Soulxrk().click()
        time.sleep(2)
        #点击返回
        Top().Back().click()
        time.sleep(1)
        #点击取消回到添加联系人页
        Top().Cancel().click()
        time.sleep(1)
        #点击我的二维码
        Top().My_qr().click()
        time.sleep(3)
        #点击其他任意处关闭二维码
        self.driver.tap([(207,1751)])
        time.sleep(2)
        #点击添加手机联系人
        Top().Add_mobile().click()
        time.sleep(2)
        #点击返回
        Top().Back().click()
        time.sleep(2)
        Top().Back().click()
        time.sleep(1)
        #点击取消
        Top().Right().click()
        time.sleep(1)

    #test6:加号点扫一扫
    def test_6(self):
        # 点击加号
        self.driver.tap([(993,165)])
        #Top().Jiahao().click()
        time.sleep(2)
        #点击扫一扫
        Top().Scan_tv().click()
        time.sleep(2)
        #点击相册按钮
        self.driver.tap([(961,166)])
        #Top().Sysxiangce().click()
        time.sleep(1)
        #选阵容二维码
        self.driver.tap([(281,490)])
        time.sleep(4)
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击群详情
        #Top().Join_group().click()
        #time.sleep(2)
        #点击返回
        #Top().Back().click()
        time.sleep(1)
        Top().Back().click()
        time.sleep(1)





if __name__=="__main__":
    unittest.main()














