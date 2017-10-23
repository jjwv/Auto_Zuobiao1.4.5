#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.Mine_main import Mine_main
from CommonFunction.SettingPage import SettingPage
from CommonFunction.MyPage import MyPage
from CommonFunction.LoginPage import LoginPage
from CommonFunction.Zhangsafe_Page import Zhangsage_Page
from CommonFunction.New_message_tixingPage import New_message_tixingPage
from CommonFunction.About_zuobiao import About_zuobiao
from Utills.GetAppiumHelp import GetAppiumHelp

#test1:账号与安全
#test2：邀我入群需要我同意
#test3：新消息提醒
#test4:多语言
#test5:关于坐标
#test6:清空所有聊天记录
#test7:退出登录
#test8：意见反馈

import unittest,time
import sys,os
sys.path.append(os.getcwd())
class Setting_Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=GetAppiumDriver().driver

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver = GetAppiumDriver().driver
        cls.driver.quit()

    def tearDown(self):
        pass

    #test1:账号与安全
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
        #点击设置
        MyPage().setting().click()
        time.sleep(1)
        #点击账号安全
        SettingPage().Z_safe().click()
        time.sleep(1)
        #点击绑定手机号
        Zhangsage_Page().Bind_mobile().click()
        time.sleep(1)
        #点击左上角。。。
        Mine_main().Right().click()
        time.sleep(1)
        #点击取消
        Zhangsage_Page().Item_tv().click()
        time.sleep(1)
        #点击返回账号与安全
        Mine_main().Back().click()
        time.sleep(1)
        #点击绑定邮箱
        Zhangsage_Page().Bind_email().click()
        time.sleep(1)
        #点击取消
        Mine_main().Back().click()
        time.sleep(1)
        #点击修改密码
        Zhangsage_Page().Modify_password().click()
        time.sleep(1)
        #点击浮窗输入原始密码
        Zhangsage_Page().Cet_input_your_pwd().send_keys("123456")
        time.sleep(1)
        #点击浮窗页确定
        Zhangsage_Page().Btn_confirm().click()
        time.sleep(1)
        #输入新密码
        Zhangsage_Page().Input_new_pwd_cet().send_keys("123456")
        time.sleep(1)
        #再次输入新密码
        Zhangsage_Page().Input_new_pwd_again_cet().send_keys("123456")
        time.sleep(1)
        #点击完成
        Mine_main().Right().click()
        time.sleep(2)

        #输入新密码
        LoginPage().password().send_keys("123456")
        # 点击登录
        time.sleep(2)
        LoginPage().login_btn().click()
        time.sleep(3)
        # 点击到我的进去我的页面
        MyPage().MyBtn().click()
        time.sleep(1)
        # 点击设置
        MyPage().setting().click()
        time.sleep(1)

    #test2：邀我入群需要我同意
    def test_2(self):
        #点击邀我入群需要我同意
        SettingPage().Invite_me_to_group_setting().click()
        time.sleep(1)
        SettingPage().Invite_me_to_group_setting().click()
        time.sleep(1)

    #test3：新消息提醒
    def test_3(self):
        #点击新消息提醒
        SettingPage().New_message_hint().click()
        time.sleep(1)
        #点击接受新消息通知
        New_message_tixingPage().News_receive().click()
        time.sleep(2)
        # 点击接受新消息通知
        New_message_tixingPage().News_receive().click()
        time.sleep(2)
        #点击声音
        New_message_tixingPage().News_sound_toggle().click()
        time.sleep(1)
        #点击震动
        New_message_tixingPage().News_vibrate_toggle().click()
        time.sleep(1)
        #点击通知显示信息详情
        New_message_tixingPage().Notify_show_detail_toggle().click()
        time.sleep(1)
        #点击勿扰模式
        New_message_tixingPage().No_disturb_toggle().click()
        time.sleep(1)
        # 点击声音
        New_message_tixingPage().News_sound_toggle().click()
        time.sleep(1)
        # 点击震动
        New_message_tixingPage().News_vibrate_toggle().click()
        time.sleep(1)
        # 点击通知显示信息详情
        New_message_tixingPage().Notify_show_detail_toggle().click()
        time.sleep(1)
        # 点击勿扰模式
        New_message_tixingPage().No_disturb_toggle().click()
        time.sleep(1)
        #点击返回
        Mine_main().Back().click()
        time.sleep(1)


    #test4:多语言
    def test_4(self):
        #点击多语言
        SettingPage().Multi_languages().click()
        time.sleep(1)
        #点击返回
        Mine_main().Back().click()
        time.sleep(1)

    #test5:关于坐标
    def test_5(self):
        #点击关于坐标
        SettingPage().About_shixin().click()
        time.sleep(1)
        #点击服务协议
        About_zuobiao().Service_agreement().click()
        time.sleep(2)
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击返回
        Mine_main().Back().click()
        time.sleep(1)
        #点击意见反馈
        About_zuobiao().Feedback_tv().click()
        time.sleep(1)
        #在输入框输入
        About_zuobiao().Feedback_et().send_keys("哈哈哈，我也不知道该说些什么")
        time.sleep(1)
        #点击提交
        About_zuobiao().Commit_btn().click()
        time.sleep(2)
        #点击返回
        Mine_main().Back().click()
        time.sleep(1)

    #test6:清空所有聊天记录
    def test_6(self):
        #点击清空所有聊天记录
        SettingPage().Clear_chat_history().click()
        time.sleep(1)
        #点击浮窗确定页
        SettingPage().Fcqd().click()
        time.sleep(1)

    #test7:退出登录
    def test_7(self):
        #点击退出登录
        SettingPage().quit().click()
        time.sleep(1)
        #点击浮窗确定
        SettingPage().qd().click()
        time.sleep(1)








if __name__=="__main__":
    unittest.main()