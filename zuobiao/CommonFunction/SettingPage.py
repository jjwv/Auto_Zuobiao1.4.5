#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class SettingPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver
    #定位账号和安全按钮
    def UserandSafe(self):
        try:
            __UserandSafe=self.driver.find_element_by_android_uiautomator('new UiSelector().text("账号与安全")')
        except Exception as err:
            assert False,\
            "账号与安全按钮定位失败"
        return __UserandSafe

     #定位退出登录按钮
    def quit(self):
        try:
            __quit=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_exit_login")
        except Exception as err:
            assert False,\
            "定位退出登录按钮失败"
        return __quit

    #浮层点击确定退出登录
    def fuceng_quie(self):
        try:
            __fuceng_quit=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/positive_tv")
        except Exception as err:
            assert False,\
            "定位浮层点击确定退出登录失败"
        return __fuceng_quit

    #定位返回按钮
    def Back(self):
        try:
            __Back=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "定位返回按钮失败"
        return __Back

    #定位完成按钮
    def Right(self):
        try:
            __Right=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
                "定位完成按钮失败"
        return __Right

    #定位账号与安全
    def Z_safe(self):
        try:
            __Z_safe=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/ll_safe")
        except Exception as err:
            assert False, \
                "定位账号与安全失败"
        return __Z_safe

   #定位入群需要我同意
    def Invite_me_to_group_setting(self):
        try:
            __Invite_me_to_group_setting=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/invite_me_to_group_setting_ll")
        except Exception as err:
            assert False, \
            "定位入群需要我同意失败"
        return __Invite_me_to_group_setting

    #定位新消息提醒
    def New_message_hint(self):
        try:
            __New_message_hint=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/ll_new_message_hint")
        except Exception as err:
            assert False, \
            "定位新消息提醒失败"
        return __New_message_hint

    #定位多语言
    def Multi_languages(self):
        try:
            __Multi_languages=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/ll_multi_languages")
        except Exception as err:
            assert False, \
            "定位多语言失败"
        return __Multi_languages

    # 定位关于坐标
    def About_shixin(self):
        try:
            __About_shixin = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/ll_about_shixin")
        except Exception as err:
            assert False, \
            "定位关于坐标失败"
        return __About_shixin

    # 定位清空所有聊天记录
    def Clear_chat_history(self):
        try:
            __Clear_chat_history = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/ll_clear_chat_history")
        except Exception as err:
            assert False, \
            "定位清空所有聊天记录失败"
        return __Clear_chat_history

    #定位清空所有聊天记录浮窗的确定键
    def Fcqd(self):
        try:
            __Fcqd = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/item_tv")
        except Exception as err:
            assert False, \
                "定位清空所有聊天记录失败"
        return __Fcqd



    # 定位退出登录的确定
    def qd(self):
        try:
            __qd = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/positive_tv")
        except Exception as err:
            assert False, \
                "定位退出登录的确定"
        return __qd

