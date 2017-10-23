#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import unittest,time
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.Email_Page import Email_Page
from Utills.GetAppiumHelp import GetAppiumHelp

#test1：添加第二个账号
#test2:发送多个收件地址的邮件
#test3:发送多个抄送地址的邮件
#test4:点击title添加账号
#test5:转发
#test6:回复
#test7：全部回复



class Email_Modeltwo(unittest.TestCase):
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

    #test1：添加第二个账号
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
        #点击邮箱
        Email_Page().Email().click()
        time.sleep(4)
        # 点击添加账号
        Email_Page().Add_Email().click()
        time.sleep(1)
        # 点击账号输入框输入正确账号
        Email_Page().ZH_shuruk().send_keys('cuiwenhao12@sina.com')
        time.sleep(1)
        # 点击密码输入框输入密码
        Email_Page().MM_shuruk().send_keys('12345678')
        # 点击确定
        Email_Page().QD().click()
        time.sleep(8)


    #test2:发送多个收件地址的邮件
    def test_2(self):
        # 点击加号
        Email_Page().Email_Jiahao().click()
        time.sleep(1)
        # 点击写邮件
        Email_Page().Xieyoujian().click()
        time.sleep(1)
        # 输入错误邮箱
        Email_Page().shoujianren().send_keys('691608216@qq.com cuiwenhaozing@sina.com shixinzuobiao@sina.com')
        time.sleep(1)
        # 输入主题
        Email_Page().Zhuti().send_keys('123')
        time.sleep(1)
        # 输入正文
        Email_Page().Zhengwen().send_keys('测试一下')
        time.sleep(1)
        # 点击发送
        Email_Page().Right().click()
        time.sleep(5)


    # test3:发送多个抄送地址的邮件
    def test_3(self):
        # 点击加号
        Email_Page().Email_Jiahao().click()
        time.sleep(1)
        # 点击写邮件
        Email_Page().Xieyoujian().click()
        time.sleep(1)
        # 输入错误邮箱
        Email_Page().shoujianren().send_keys('691608216@qq.com')
        time.sleep(1)
        #输入抄送
        Email_Page().Chaosong().send_keys('cuiwenhaozing@sina.com shixinzuobiao@sina.com xianglei@shixinyun.com gongyufei@shixinyun.com fanshaohua@shixinyun.com ')
        # 输入主题
        Email_Page().Zhuti().send_keys('123')
        time.sleep(1)
        # 输入正文
        Email_Page().Zhengwen().send_keys('测试一下')
        time.sleep(1)
        # 点击发送
        Email_Page().Right().click()
        time.sleep(6)

    #test4:点击title添加账号
    def test_4(self):
        #点击账号title
        Email_Page().Zhanghao_Title().click()
        time.sleep(1)
        #点击添加邮箱账号
        Email_Page().Title_Tianjiazhanghao().click()
        time.sleep(1)
        # 输入账号
        Email_Page().ZH_shuruk().send_keys('fanshaohuashixin@sina.com')
        time.sleep(1)
        # 输入密码
        Email_Page().MM_shuruk().send_keys('fsh123456')
        # 点击确定
        Email_Page().QD().click()
        time.sleep(17)

    # test5:转发
    def test_5(self):
        time.sleep(2)
        #点击第一个邮件
        self.driver.tap([(408,519)])
        time.sleep(7)
        #点击转发
        Email_Page().Zhuanfa().click()
        time.sleep(1)
        #输入邮箱
        Email_Page().shoujianren().send_keys('691608216@qq.com')
        time.sleep(1)
        # 输入正文
        #Email_Page().Zhengwen().send_keys('测试')
        time.sleep(1)
        #点击发送
        Email_Page().Right().click()
        time.sleep(4)

    #test6：回复
    def test_6(self):
        #点击第一个邮件
        #self.driver.tap([(550,516)])
        time.sleep(3)
        #点击回复
        Email_Page().Huifu().click()
        time.sleep(2)
        #点击回复
        Email_Page().Fuchaugn_Huifu().click()
        time.sleep(3)
        #点击发送
        Email_Page().Right().click()
        time.sleep(1)
        #点击返回
        Email_Page().Back().click()
        time.sleep(1)

    #test7:全部回复
    def test_7(self):
        # 点击第一个邮件
        self.driver.tap([(550, 516)])
        time.sleep(3)
        # 点击回复
        Email_Page().Huifu().click()
        time.sleep(2)
        #点击全部回复：
        Email_Page().Fuchaugn_Quanbuhuifu().click()
        time.sleep(2)
        #点击发送
        Email_Page().Right().click()
        time.sleep(3)
        # 点击返回
        Email_Page().Back().click()
        time.sleep(5)

    #test8:删除全部用户
    def test_8(self):
        #点击加号
        Email_Page().Email_Jiahao().click()
        time.sleep(1)
        #点击账号管理
        Email_Page().Zhanghaogl().click()
        time.sleep(1)
        #点击一个账号
        Email_Page().Zhanghaogl_Zz().click()
        time.sleep(1)
        #点击删除账号
        Email_Page().Shanchuzhanghao().click()
        time.sleep(1)
        #点击弹窗中的删除账号
        Email_Page().Tanchuang_Shanchuzhanghao().click()
        time.sleep(7)
        # 点击邮箱
        Email_Page().Email().click()
        time.sleep(10)
        # 点击加号
        Email_Page().Email_Jiahao().click()
        time.sleep(1)
        # 点击账号管理
        Email_Page().Zhanghaogl().click()
        time.sleep(1)
        # 点击一个账号
        Email_Page().Zhanghaogl_Zz().click()
        time.sleep(1)
        # 点击删除账号
        Email_Page().Shanchuzhanghao().click()
        time.sleep(1)
        # 点击弹窗中的删除账号
        Email_Page().Tanchuang_Shanchuzhanghao().click()
        time.sleep(4)








