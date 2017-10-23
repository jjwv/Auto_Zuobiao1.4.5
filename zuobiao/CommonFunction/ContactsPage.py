#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class ContactPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位联系人
    def Contact(self):
        try:
            __Contact=self.driver.find_element_by_android_uiautomator('new UiSelector().text("联系人")')
        except Exception as err:
            assert False,\
            "定位联系人错误"
        return __Contact

    #定位我的好友分组
    def Myfriend(self):
        try:
            __Myfrien=self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的好友")')
        except Exception as err:
            assert False,\
            "定位我的好友分组失败"
        return __Myfrien

    #定位好友分组的好友
    def Friend(self):
        try:
            __Friend=self.driver.find_element_by_android_uiautomator('new UiSelector().text("红鲤鱼与绿鲤鱼与驴")')
        except Exception as err:
            assert False,\
            "定位好友分组的红鲤鱼与绿鲤鱼与驴失败"
        return __Friend

    #长按好友分组弹出窗点击管理分组
    def Glfz(self):
        try:
            __Glfz=self.driver.find_element_by_android_uiautomator('new UiSelector().text("分组管理")')
        except Exception as err:
            assert False,\
            "定位分组管理"
        return __Glfz

 #定位好友分组的蒋先生
    def Jxs(self):
        try:
            __Jxs=self.driver.find_element_by_android_uiautomator('new UiSelector().text("蒋先生")')
        except Exception as err:
            assert False,\
            "定位好友分组的蒋先生失败"
        return __Jxs

 #定位好友分组的项雷
    def Xianglei(self):
        try:
            __Xianglei=self.driver.find_element_by_android_uiautomator('new UiSelector().text("项雷")')
        except Exception as err:
            assert False,\
            "定位好友分组的项雷失败"
        return __Xianglei

        # 定位好友分组的项雷123
    def Xiangleione(self):
        try:
            __Xiangleione = self.driver.find_element_by_android_uiautomator('new UiSelector().text("项雷123")')
        except Exception as err:
            assert False, \
                "定位好友分组的项雷123失败"
        return __Xiangleione

    #定位万水千山总是情
    def Wanshui(self):
        try:
            __Wanshui = self.driver.find_element_by_android_uiautomator('new UiSelector().text("万水千山总是情")')
        except Exception as err:
            assert False, \
                "定位万水千山总是情失败"
        return __Wanshui

    #定位一起开黑
    def Yqkh(self):
        try:
            __Yqkh = self.driver.find_element_by_android_uiautomator('new UiSelector().text("一起开黑")')
        except Exception as err:
            assert False, \
                "定位一起开黑失败"
        return __Yqkh


    #定位菲姐
    def Fj(self):
        try:
            __Fj = self.driver.find_element_by_android_uiautomator('new UiSelector().text("菲姐")')
        except Exception as err:
            assert False, \
                "定位菲姐失败"
        return __Fj


    #定位a老范
    def LF(self):
        try:
            __LF = self.driver.find_element_by_android_uiautomator('new UiSelector().text("阿老范")')
        except Exception as err:
            assert False, \
                "定位阿老范失败"
        return __LF

  #定位宫雨菲非
    def gyff(self):
        try:
            __gyff = self.driver.find_element_by_android_uiautomator('new UiSelector().text("宫雨非非")')
        except Exception as err:
            assert False, \
                "定位宫雨菲非失败"
        return __gyff

    #定位冯瑞芳
    def frf(self):
        try:
            __frf = self.driver.find_element_by_android_uiautomator('new UiSelector().text("冯瑞芳")')
        except Exception as err:
            assert False, \
                "定位冯瑞芳失败"
        return __frf

    #定位开玩笑
    def kwx(self):
        try:
            __kwx = self.driver.find_element_by_android_uiautomator('new UiSelector().text("开玩笑")')
        except Exception as err:
            assert False, \
                "定位开玩笑失败"
        return __kwx
    #定位李志飞
    def lzf(self):
        try:
            __lzf = self.driver.find_element_by_android_uiautomator('new UiSelector().text("李志飞")')
        except Exception as err:
            assert False, \
                "定位李志飞失败"
        return __lzf

    #定位PC张彩蝶
    def zcd(self):
        try:
            __zcd = self.driver.find_element_by_android_uiautomator('new UiSelector().text("PC张彩蝶")')
        except Exception as err:
            assert False, \
                "定位张彩蝶失败"
        return __zcd

    #定位倩姐
    def qj(self):
        try:
            __qj = self.driver.find_element_by_android_uiautomator('new UiSelector().text("倩姐")')
        except Exception as err:
            assert False, \
                "定位倩姐失败"
        return __qj

    #定位孙登岭
    def sdl(self):
        try:
            __sdl = self.driver.find_element_by_android_uiautomator('new UiSelector().text("孙登岭")')
        except Exception as err:
            assert False, \
                "定位孙登岭失败"
        return __sdl


#

