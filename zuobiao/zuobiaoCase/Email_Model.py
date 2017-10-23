#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import unittest,time
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.Email_Page import Email_Page
from Utills.GetAppiumHelp import GetAppiumHelp

#test1：进入邮箱添加邮箱账号  错误邮箱账号正确密码
#test2:添加正确的邮箱账号和错误密码
#test3:添加正确的账号和密码
#test4:发送邮件  输入错误邮箱地址 有主题
#test5:输入正确收件人地址，不输入主题
#test6:输入正确邮箱地址，不输入主题，发送邮件
#test7:存入草稿箱
#test_8:进入草稿箱，发送草稿
#test9:查看已发送，然后删除账号

class Email_Model(unittest.TestCase):
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

    #test1：进入邮箱添加邮箱账号  错误邮箱账号正确密码
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
        time.sleep(2)
        #点击添加账号
        Email_Page().Add_Email().click()
        time.sleep(2)
        #点击账号输入框输入错误账号
        Email_Page().ZH_shuruk().send_keys('hcuiwenhaozing@sina.com')
        time.sleep(1)
        #点击密码输入框输入密码
        Email_Page().MM_shuruk().send_keys('idontloveyou')
        #点击确定
        Email_Page().QD().click()
        time.sleep(6)
        # 点击添加失败中的确定
        Email_Page().Tjsb_Qd().click()
        time.sleep(2)
        Email_Page().MM_shuruk().clear()
        time.sleep(3)
        self.driver.tap([(972, 519)])
        time.sleep(1)



    # test2:添加正确的邮箱账号和错误密码
    def test_2(self):
        # 点击账号输入框输入正确账号
        Email_Page().ZH_shuruk().send_keys('cuiwenhaozing@sina.com')
        time.sleep(1)
        # 点击密码输入框输入错误密码
        Email_Page().MM_shuruk().send_keys('hahaidontloveyou')
        # 点击确定
        Email_Page().QD().click()
        time.sleep(6)
        #点击添加失败中的确定
        Email_Page().Tjsb_Qd().click()
        time.sleep(2)
        Email_Page().MM_shuruk().clear()
        time.sleep(1)
        self.driver.tap([(972,519)])
        time.sleep(1)


    # test3:添加正确的账号和密码
    def test_3(self):
        # 点击账号输入框输入正确账号
        Email_Page().ZH_shuruk().send_keys('shixinzuobiao@sina.com')
        time.sleep(1)
        # 点击密码输入框输入正确密码
        Email_Page().MM_shuruk().send_keys('12345678')
        # 点击确定
        Email_Page().QD().click()
        
        time.sleep(10)

    #test4:发送邮件  输入错误邮箱地址 有主题
    def test_4(self):
        #点击加号
        Email_Page().Email_Jiahao().click()
        time.sleep(1)
        #点击写邮件
        Email_Page().Xieyoujian().click()
        time.sleep(1)
        #输入错误邮箱
        Email_Page().shoujianren().send_keys('691608216@.com')
        time.sleep(1)
        #输入主题
        Email_Page().Zhuti().send_keys('123')
        time.sleep(1)
        #输入正文
        Email_Page().Zhengwen().send_keys('测试一下')
        time.sleep(1)
        #点击发送
        Email_Page().Right().click()
        time.sleep(1)
        #点击提示框中的确定
        Email_Page().Tishikuang_Qd().click()
        time.sleep(2)


    # test5:输入正确收件人地址，发送邮件
    def test_5(self):
        Email_Page().shoujianren().clear()
        time.sleep(3)
        # 输入正确邮箱
        Email_Page().shoujianren().send_keys('cuiwenhaozing@sina.com')
        time.sleep(1)
        #点击发送
        Email_Page().Right().click()
        
        time.sleep(3)

    #test6:输入正确邮箱地址，不输入主题，发送邮件
    def test_6(self):
        # 点击加号
        Email_Page().Email_Jiahao().click()
        time.sleep(1)
        # 点击写邮件
        Email_Page().Xieyoujian().click()
        time.sleep(1)
        #输入正确邮箱
        Email_Page().shoujianren().send_keys('691608216@qq.com')
        time.sleep(1)
        #输入正文
        Email_Page().Zhengwen().send_keys('测试')
        time.sleep(1)
        #点击发送
        Email_Page().Right().click()
        time.sleep(6)


    #test7:存入草稿箱
    def test_7(self):
        #点击取消存入草稿
        Email_Page().Back().click()
        time.sleep(2)
        #点击保存草稿
        Email_Page().Baocuncg().click()
        time.sleep(3)

    #test_8:进入草稿箱，发送草稿
    def test_8(self):
        #向左划进入草稿箱
        GetAppiumHelp().RightToLeft()
        time.sleep(1)
        #点击刚存入草稿箱的邮件
        self.driver.tap([(520,560)])
        time.sleep(3)
        #输入主题
        Email_Page().Zhuti().send_keys('测试')
        time.sleep(1)
        #点击发送
        Email_Page().Right().click()

        time.sleep(4)

    #test9:查看已发送，然后删除账号
    def test_9(self):
        #右划到已发送
        GetAppiumHelp().RightToLeft()
        time.sleep(1)
        GetAppiumHelp().RightToLeft()
        time.sleep(3)
        #查看刚发送的邮件
        self.driver.tap([(520, 560)])
        time.sleep(5)
        #返回已发送
        Email_Page().Back().click()
        time.sleep(1)
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
        time.sleep(4)














