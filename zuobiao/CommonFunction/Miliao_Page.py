#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
class Miliao_Page(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

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


    #定位聊天窗口中的加号
    def Jiahao_Miliao(self):
        try:
            __Jiahao_Miliao = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_more_btn")
        except Exception as err:
            assert False, \
            "定位聊天窗口中的加号"
        return __Jiahao_Miliao

    #定位密聊按钮
    def Miliao(self):
        try:
            __Miliao = self.driver.find_element_by_android_uiautomator('new UiSelector().text("密聊")')
        except Exception as err:
            assert False, \
            "定位密聊按钮"
        return __Miliao

    # 定位密聊文本输入框
    def Miliao_Shurukuang(self):
        try:
            __Miliao_Shurukuang= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_message_et")
        except Exception as err:
            assert False, \
                "定位密聊文本输入框"
        return __Miliao_Shurukuang

    # 定位密聊文本发送
    def Miliao_Fasong(self):
        try:
            __Miliao_Fsong= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_send_btn")
        except Exception as err:
            assert False, \
                "定位定位密聊文本发送"
        return __Miliao_Fsong

    # 定位放大镜全局搜索
    def Fangdajing_Sousu(self):
        try:
            __Fangdajing_Sousu= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/logo")
        except Exception as err:
            assert False, \
                "定位放大镜全局搜索"
        return __Fangdajing_Sousu
    # 定位放大镜全局搜索 输入框
    def Fangdajing_Shurukuang(self):
        try:
            __Fangdajing_Shorukuang= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_layout")
        except Exception as err:
            assert False, \
                "定位放大镜全局搜索 输入框"
        return __Fangdajing_Shorukuang

        # 定位放大镜全局搜索 真输入框
    def Fangdajing_Zhensrk(self):
        try:
            __Fangdajing_Zhensrk = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_edt")
        except Exception as err:
            assert False, \
                "定位放大镜全局搜索 真输入框"
        return __Fangdajing_Zhensrk


     # 定位放大镜全局搜索 输入框 取消按钮
    def Fangdajing_Quxiao(self):
        try:
            __Fangdajing_Quxiao= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        except Exception as err:
            assert False, \
                "定位放大镜全局搜索 输入框 取消按钮"
        return __Fangdajing_Quxiao



