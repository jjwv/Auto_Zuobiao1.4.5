#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class New_message_tixingPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位接受新消息通知
    def News_receive(self):
        try:
            __News_receive=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/news_receive_msg_toggle")
        except Exception as err:
            assert False,\
            "定位接受新消息通知失败"
        return __News_receive

    #定位声音
    def News_sound_toggle(self):
        try:
            __News_sound_toggle=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/news_sound_toggle")
        except Exception as err:
            assert False,\
            "定位接受新消息通知失败"
        return __News_sound_toggle

    #定位震动
    def News_vibrate_toggle(self):
        try:
            __News_vibrate_toggle=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/news_vibrate_toggle")
        except Exception as err:
            assert False,\
            "定位震动失败"
        return __News_vibrate_toggle

    #定位通知显示信息详情
    def Notify_show_detail_toggle(self):
        try:
            __Notify_show_detail_toggle=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/notify_show_detail_toggle")
        except Exception as err:
            assert False,\
            "定位通知显示信息详情"
        return __Notify_show_detail_toggle

    #定位勿扰模式
    def No_disturb_toggle(self):
        try:
            __No_disturb_toggle=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/no_disturb_toggle")
        except Exception as err:
            assert False,\
            "定位勿扰模式"
        return __No_disturb_toggle