#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.MyPage import MyPage
from CommonFunction.LoginPage import LoginPage
from CommonFunction.Mine_main import Mine_main
from CommonFunction.My_Headpage import My_Headpage
from CommonFunction.Job_information import Job_information
from Utills.GetAppiumHelp import GetAppiumHelp

#test1:进入个人中心修改头像
#test2:修改昵称
#test3：二维码名片
#test4:更改性别
#test5:更改生日
#test6:更改地区
#test7:工作信息(行业，公司，职位）
#test8:更改电话
#test9:更改邮箱

import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class My_Model(unittest.TestCase):
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

    # test1:进入个人中心修改头像
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
        #点击进入个人中心
        MyPage().Mine_mine().click()
        time.sleep(1)
        #点击头像
        Mine_main().Head().click()
        time.sleep(1)
        #点击。。。
        #Mine_main().Right().click()
        #长按出现换头像菜单
        self.driver.tap([(200,1000)],1000)
        time.sleep(1)
        #点击从相册选择
        #My_Headpage().Cong_Xz().click()
        self.driver.tap([(460,1479)])
        time.sleep(1)
        #点击选择 图片
        self.driver.tap([(383,808)])
        time.sleep(1)
        #点击图片
        self.driver.tap([(419,358)])
        time.sleep(1)
        #点击完成
        self.driver.tap([(742,164)])
        time.sleep(5)
        '''
        # 点击头像
        Mine_main().Head().click()
        time.sleep(1)
        # 点击。。。
        Mine_main().Right().click()
        time.sleep(1)
        #点击保存照片
        My_Headpage().Baoc_Zp().click()
        time.sleep(1)
        #点击返回个人中心
        Mine_main().Back().click()
        time.sleep(1)
        '''

    #test2:修改昵称
    def test_2(self):
        #点击昵称
        Mine_main().UserName().click()
        time.sleep(1)
        #点击昵称的输入框
        Mine_main().Input_nickname().send_keys("榴莲牛奶流沙包")
        time.sleep(1)
        #点击保存
        Mine_main().Right().click()
        time.sleep(3)

    # test3：二维码名片
    def test_3(self):
        #点击二维码
        Mine_main().Qr_code_ll().click()
        time.sleep(1)
        #点击保存到手机
        Mine_main().Save_to_mobile().click()
        time.sleep(1)
        #点击分享二维码
        Mine_main().Share_qr().click()
        time.sleep(1)
        #点击返回
        Mine_main().Back().click()
        time.sleep(1)
        #返回
        Mine_main().Back().click()
        time.sleep(1)

    # test4:更改性别
    def test_4(self):
        #点击性别
        Mine_main().Gender_tv().click()
        time.sleep(1)
        #点击男
        self.driver.tap([(542,1680)])
        #Mine_main().nan().click()
        time.sleep(2)

    #test5：更改生日
    def test_5(self):
        #定位生日
        Mine_main().Birthday().click()
        time.sleep(1)
        #点击滑屏
        self.driver.swipe(178,1790,180,1455,800)
        time.sleep(1)
        self.driver.swipe(900,1800,900,1490,800)
        time.sleep(1)
        #点击确定
        Mine_main().BtnSubmit().click()
        time.sleep(2)

    #test6:更改地区
    def test_6(self):
        #点击地区
        Mine_main().Area().click()
        time.sleep(1)
        #滑屏
        self.driver.swipe(251,1825,251,1550,700)
        time.sleep(1)
        self.driver.swipe(790,1825,790,1550,700)
        time.sleep(1)
        #点击确定
        Mine_main().BtnSubmit().click()
        time.sleep(1)

    #test7:工作信息
    def test_7(self):
        #点击工作信息
        MyPage().Job_in().click()
        time.sleep(1)
        #点击行业
        Job_information().Industry().click()
        time.sleep(1)
        #点击计算机
        Job_information().Jsuanji().click()
        time.sleep(1)
        #点击完成
        Mine_main().Right().click()
        time.sleep(1)

        #点击公司
        Job_information().Company().click()
        time.sleep(1)
        #修改公司名 点击输入框
        Job_information().Gshurukuang().send_keys("时信互联")
        time.sleep(1)
        #点击确定
        Mine_main().Right().click()
        time.sleep(1)

        #点击职位
        Job_information().Position().click()
        time.sleep(1)
        #输入测试
        Job_information().Gshurukuang().send_keys("测试")
        time.sleep(1)
        #点击完成
        Mine_main().Right().click()
        time.sleep(1)
        #点击返回
        Mine_main().Back().click()
        time.sleep(1)

    #test8:更改电话
    def test_8(self):
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击电话
        Mine_main().Iphone().click()
        time.sleep(1)
        #点击输入框输入手机号
        Mine_main().Dsrk().send_keys("13601515688")
        time.sleep(1)
        #点击确定
        Mine_main().Right().click()
        time.sleep(1)

    #test9:更改邮箱
    def test_9(self):
        #点击邮箱
        Mine_main().Email().click()
        time.sleep(1)
        #输入邮箱
        Mine_main().Ysrk().send_keys("cuiwenhaozing@163.com")
        time.sleep(1)
        #点击确定
        Mine_main().Right().click()
        time.sleep(1)



        

if __name__ == "__main__":
    unittest.main()





