#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class MessagePage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位消息模块页
    def Message(self):
        try:
            __Message=self.driver.find_element_by_android_uiautomator('new UiSelector().text("消息")')
        except Exception as err:
            assert False,\
            "定位消息模块失败"
        return __Message

    #定位红鲤鱼资料详情页发送消息
    def SendMessage(self):
        try:
            __SendMessage=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/send_message_layout")
        except Exception as err:
            assert False,\
            "定位红鲤鱼资料详情页发送消息失败"
        return __SendMessage

    #定位红鲤鱼资料详情页语音呼叫失
    def SendVoice(self):
        try:
            __SendVoice = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/voic_rlayout")
        except Exception as err:
            assert False, \
            "定位红鲤鱼资料详情页语音呼叫失败"
        return __SendVoice

    #定位消息页面输入框
    def Chat_Message(self):
        try:
            __Chat_Message=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_message_et")
        except Exception as err:
            assert False,\
            "定位消息页面输入框失败"
        return __Chat_Message

    #定位消息页面发送按钮
    def Chat_Send(self):
        try:
            __Chat_Send=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_send_btn")
        except Exception as err:
            assert False,\
            "定位消息页面发送按钮失败"
        return __Chat_Send

    #定位语音按钮
    def Chat_Voice(self):
        try:
            __Chat_Voice=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_voice_btn")
        except Exception as err:
            assert False,\
            "定位语音按钮失败"
        return __Chat_Voice

    #定位按住说话
    def btn_record(self):
        try:
            __btn_record=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_record")
        except Exception as err:
            assert False,\
            "定位按住说话失败"
        return __btn_record

    #定位松开试听按钮
    def playView(self):
        try:
            __playView=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/img_playView")
        except Exception as err:
            assert False,\
            "定位松开试听失败"
        return __playView

    #定位松开删除按钮
    def delView(self):
        try:
            __delView=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/img_delView")
        except Exception as err:
            assert False,\
            "定位松开删除按钮"
        return __delView

    #定位试听播放按钮
    def shiting(self):
        try:
            __shiting=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_play")
        except Exception as err:
            assert False,\
            "定位试听播放按钮"
        return __shiting
    #定位试听发送按钮
    def shifasong(self):
        try:
            __shifasong=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_send")
        except Exception as err:
            assert False,\
            "定位试听发送按钮"
        return __shifasong

    # 定位试听取消
    def shiquxiao(self):
        try:
            __shiquxiao = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_cancel")
        except Exception as err:
            assert False, \
            "定位试听取消"
        return __shiquxiao






