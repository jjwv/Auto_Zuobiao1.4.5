#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Sum(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位加号按钮
    def jiahao(self):
        try:
            __jiahao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_more_btn")
        except Exception as err:
            assert False,\
            "定位加号按钮失败"
        return __jiahao
    #定位语音通话
    def Yunyin(self):
        try:
            __Yunyin=self.driver.find_element_by_android_uiautomator('new UiSelector().text("语音通话")')
        except Exception as err:
            assert False,\
            "定位语音通话失败"
        return __Yunyin

    #定位语音通话页面免提
    def Mianti(self):
        try:
            __Mianti=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/call_switch_speaker_btn")
        except Exception as err:
            assert False,\
            "定位语音通话页面免提失败"
        return __Mianti

    #定位语音通话取消按钮
    def Quxiao(self):
        try:
            __Quxiao = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/call_cancel_btn")
        except Exception as err:
            assert False, \
             "定位语音通话取消按钮失败"
        return __Quxiao

    #定位语音通话静音按钮
    def Jingyin(self):
        try:
            __Jingyin = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/call_switch_mute_btn")
        except Exception as err:
            assert False, \
            "定位语音通话静音按钮失败"
        return __Jingyin

    #定位视频通话
    def Shipin(self):
        try:
            __Shipin=self.driver.find_element_by_android_uiautomator('new UiSelector().text("视频通话")')
        except Exception as err:
            assert False,\
            "定位视频通话失败"
        return __Shipin

